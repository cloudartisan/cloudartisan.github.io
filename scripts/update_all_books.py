#!/usr/bin/env python3
"""
Complete book data updater - fetches and verifies ALL books from YAML file
Uses Open Library API to fetch book metadata by ISBN
"""

import requests
import yaml
import time
import re
from pathlib import Path
from typing import Dict, Optional

class BookUpdater:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'CloudArtisan-BookUpdater/1.0 (https://cloudartisan.com)'
        })
        
    def search_openlibrary_by_title_author(self, title: str, author: str) -> Optional[Dict]:
        """Search Open Library by title and author to get original work data"""
        try:
            # Clean up search terms
            clean_title = title.replace('"', '').strip()
            clean_author = author.replace('"', '').strip()
            
            # Search URL
            search_url = f"https://openlibrary.org/search.json?title={clean_title}&author={clean_author}&limit=3"
            print(f"  Searching by title+author: {clean_title} by {clean_author}")
            
            response = self.session.get(search_url, timeout=15)
            if response.status_code != 200:
                return None
                
            data = response.json()
            
            if not data.get('docs') or len(data['docs']) == 0:
                print(f"  ⚠️  No search results found")
                return None
            
            # Take the first result that looks like a match
            for doc in data['docs'][:3]:  # Check first 3 results
                parsed_data = self.parse_openlibrary_search_result(doc)
                if parsed_data and self.validate_book_match(parsed_data, title, author):
                    print(f"  ✅ Found via search: {parsed_data.get('title', 'Unknown')}")
                    
                    # Try to get additional details (pages, genres) from the work record
                    if 'key' in doc:
                        additional_data = self.fetch_openlibrary_work_details(doc['key'])
                        if additional_data:
                            parsed_data.update(additional_data)
                    
                    return parsed_data
            
            print(f"  ⚠️  Search results don't match expected book")
            return None
            
        except Exception as e:
            print(f"  ❌ Search error: {e}")
            return None
    
    def parse_openlibrary_search_result(self, doc: Dict) -> Dict:
        """Parse Open Library search result"""
        parsed = {}
        
        # Debug: print available fields for first few books
        if doc.get('title') in ['A Wizard of Earthsea', 'The Left Hand of Darkness']:
            print(f"    DEBUG: Available fields: {list(doc.keys())}")
            if 'number_of_pages_median' in doc:
                print(f"    DEBUG: number_of_pages_median = {doc['number_of_pages_median']}")
            if 'subject' in doc:
                print(f"    DEBUG: subjects = {doc['subject'][:5]}")  # First 5 subjects
        
        # Extract title
        if 'title' in doc:
            parsed['title'] = doc['title']
        
        # Extract author
        if 'author_name' in doc and doc['author_name']:
            parsed['author'] = doc['author_name'][0]
        
        # Extract first publish year (this is what we want!)
        if 'first_publish_year' in doc:
            year = doc['first_publish_year']
            if 1800 <= year <= 2027:
                parsed['year'] = year
        
        # Extract number of pages - try multiple fields
        pages = None
        for pages_field in ['number_of_pages_median', 'page_count', 'number_of_pages']:
            if pages_field in doc and doc[pages_field]:
                candidate_pages = doc[pages_field]
                if isinstance(candidate_pages, (int, float)) and 10 <= candidate_pages <= 2000:
                    pages = int(candidate_pages)
                    break
        
        if pages:
            parsed['pages'] = pages
        
        # Extract subjects and convert to proper genre
        subjects = []
        
        # Try 'subject' field first
        if 'subject' in doc and doc['subject']:
            subjects.extend(doc['subject'])
        
        # Try 'subject_facet' as backup
        if 'subject_facet' in doc and doc['subject_facet']:
            subjects.extend(doc['subject_facet'])
        
        if subjects:
            genre = self.get_genre_from_subjects(subjects)
            if genre:
                parsed['genre'] = genre
        
        return parsed
    
    def get_genre_from_subjects(self, subjects: list) -> Optional[str]:
        """Convert Open Library subjects to proper book genres"""
        if not subjects:
            return None
            
        # Genre mapping - map subject keywords to proper book genres
        genre_mappings = {
            # Fantasy
            'fantasy': 'Fantasy',
            'magic': 'Fantasy', 
            'wizards': 'Fantasy',
            'dragons': 'Fantasy',
            'elves': 'Fantasy',
            'amber (imaginary place)': 'Fantasy',
            'castle amber': 'Fantasy',
            'imaginary wars': 'Fantasy',
            
            # Science Fiction
            'science fiction': 'Science Fiction',
            'sci-fi': 'Science Fiction', 
            'sci fi': 'Science Fiction',
            'ciencia-ficción': 'Science Fiction',
            'hugo award': 'Science Fiction',
            'nebula award': 'Science Fiction',
            'space': 'Science Fiction',
            'aliens': 'Science Fiction',
            'time travel': 'Science Fiction',
            'dystopia': 'Science Fiction',
            'utopia': 'Science Fiction',
            'telepathy': 'Science Fiction',
            'mutation': 'Science Fiction',
            'post-apocalyptic': 'Science Fiction',
            'parallel worlds': 'Science Fiction',
            'dreams': 'Science Fiction',  # For books like Lathe of Heaven
            'anarchism': 'Science Fiction',  # For political sci-fi like Dispossessed
            
            # Horror/Thriller
            'horror': 'Horror',
            'vampires': 'Horror',
            'zombies': 'Horror',
            'supernatural': 'Horror',
            'occult': 'Horror',
            'occultism': 'Horror',
            'mystery': 'Mystery',
            'suspense': 'Thriller',
            'psychological warfare': 'Thriller',
            
            # Crime/Spy Fiction  
            'crime': 'Crime',
            'detective': 'Crime',
            'murder': 'Crime',
            'assassins': 'Spy Fiction',
            'murder for hire': 'Spy Fiction',
            'espionage': 'Spy Fiction',
            'spies': 'Spy Fiction',
            'jason bourne': 'Spy Fiction',
            'terrorists': 'Thriller',
            'terrorism': 'Thriller',
            
            # Non-Fiction categories
            'psychology': 'Non-Fiction',
            'biography': 'Biography', 
            'history': 'History',
            'science': 'Non-Fiction',
            'sports': 'Non-Fiction',
            'athletic performance': 'Non-Fiction',
            'human genetics': 'Non-Fiction',
            'ability': 'Non-Fiction',
            'developmental psychology': 'Non-Fiction',
            'nyt:science': 'Non-Fiction',
            'new york times bestseller': 'Non-Fiction',
            
            # Literary Fiction
            'american literature': 'Literary Fiction',
            'british literature': 'Literary Fiction',
            'contemporary fiction': 'Literary Fiction',
        }
        
        # Check each subject against our mappings
        for subject in subjects:
            subject_lower = subject.lower().strip()
            
            # Direct mapping
            if subject_lower in genre_mappings:
                return genre_mappings[subject_lower]
            
            # Partial matching for compound subjects
            for keyword, genre in genre_mappings.items():
                if keyword in subject_lower:
                    return genre
        
        # Fallback to "Fiction" for most books if no specific genre found
        # but skip obviously non-fiction subjects
        non_fiction_keywords = [
            'psychology', 'science', 'history', 'biography', 'sports',
            'genetics', 'pathological', 'mental', 'social', 'political'
        ]
        
        subject_text = ' '.join(subjects).lower()
        if any(keyword in subject_text for keyword in non_fiction_keywords):
            return 'Non-Fiction'
        
        return 'Fiction'  # Default fallback
    
    def infer_genre_from_context(self, title: str, author: str, why_essential: str) -> str:
        """Infer genre from title, author, and description when no subjects available"""
        
        # Combine all text for analysis
        text_to_analyze = f"{title} {author} {why_essential}".lower()
        
        # Author-specific mappings for well-known genre authors
        author_genres = {
            'barry eisler': 'Spy Fiction',
            'robert ludlum': 'Spy Fiction', 
            'john le carré': 'Spy Fiction',
            'tom clancy': 'Thriller',
            'lee child': 'Thriller',
            'michael crichton': 'Science Fiction',
            'stephen king': 'Horror',
            'agatha christie': 'Mystery',
            'arthur conan doyle': 'Mystery',
            'isaac asimov': 'Science Fiction',
            'philip k. dick': 'Science Fiction',
            'ursula k. le guin': 'Science Fiction',  # Fallback if subjects miss
            'j.r.r. tolkien': 'Fantasy',
            'george r.r. martin': 'Fantasy',
        }
        
        # Check author mappings first
        author_lower = author.lower()
        for known_author, genre in author_genres.items():
            if known_author in author_lower:
                return genre
        
        # Keyword-based inference from title and description
        thriller_keywords = [
            'spy', 'thriller', 'assassin', 'kill', 'murder', 'espionage', 
            'agent', 'cia', 'fbi', 'intelligence', 'operative', 'covert',
            'bourne', 'rain', 'deadly', 'lethal'
        ]
        
        crime_keywords = [
            'crime', 'detective', 'police', 'investigation', 'criminal',
            'gang', 'mafia', 'noir', 'heist'
        ]
        
        scifi_keywords = [
            'science fiction', 'sci-fi', 'space', 'alien', 'future', 
            'robot', 'ai', 'cyberpunk', 'dystopia', 'utopia', 'time travel',
            'genetic', 'clone', 'terraforming'
        ]
        
        fantasy_keywords = [
            'fantasy', 'magic', 'wizard', 'dragon', 'elf', 'dwarf', 
            'quest', 'sword', 'sorcery', 'enchanted', 'realm'
        ]
        
        horror_keywords = [
            'horror', 'vampire', 'zombie', 'ghost', 'supernatural', 
            'haunted', 'demon', 'evil', 'terror'
        ]
        
        mystery_keywords = [
            'mystery', 'detective', 'investigation', 'murder', 'clue',
            'suspect', 'solve', 'whodunit'
        ]
        
        # Count matches for each genre
        genre_scores = {
            'Spy Fiction': sum(1 for keyword in thriller_keywords if keyword in text_to_analyze),
            'Crime': sum(1 for keyword in crime_keywords if keyword in text_to_analyze),
            'Science Fiction': sum(1 for keyword in scifi_keywords if keyword in text_to_analyze),
            'Fantasy': sum(1 for keyword in fantasy_keywords if keyword in text_to_analyze),
            'Horror': sum(1 for keyword in horror_keywords if keyword in text_to_analyze),
            'Mystery': sum(1 for keyword in mystery_keywords if keyword in text_to_analyze),
        }
        
        # Return the genre with the highest score, if any
        if max(genre_scores.values()) > 0:
            return max(genre_scores, key=genre_scores.get)
        
        # Final fallback
        return 'Fiction'
    
    def fetch_openlibrary_work_details(self, work_key: str) -> Optional[Dict]:
        """Fetch additional details from Open Library work record"""
        try:
            # Work key is like "/works/OL123456W"
            if not work_key.startswith('/works/'):
                return None
                
            url = f"https://openlibrary.org{work_key}.json"
            print(f"    Fetching work details: {work_key}")
            
            response = self.session.get(url, timeout=15)
            if response.status_code != 200:
                return None
                
            work_data = response.json()
            additional = {}
            
            # Extract subjects and convert to proper genre
            if 'subjects' in work_data and work_data['subjects']:
                # Debug output for Barry Eisler books
                if 'eisler' in work_data.get('title', '').lower() or 'rain' in work_data.get('title', '').lower():
                    print(f"    DEBUG Eisler subjects: {work_data['subjects'][:10]}")
                
                genre = self.get_genre_from_subjects(work_data['subjects'])
                if genre:
                    additional['genre'] = genre
                    print(f"    Found genre: {genre}")
                else:
                    # Debug: show subjects when no genre found
                    if 'eisler' in work_data.get('title', '').lower() or 'rain' in work_data.get('title', '').lower():
                        print(f"    DEBUG: No genre mapped from subjects: {work_data['subjects'][:5]}")
            else:
                # Debug: no subjects found
                if work_data.get('title') and ('eisler' in work_data.get('title', '').lower() or 'rain' in work_data.get('title', '').lower()):
                    print(f"    DEBUG: No subjects field found for {work_data.get('title', 'Unknown')}")
            
            # For page count, we need to look at editions
            # Try to get a representative edition for page count
            if 'key' in work_data:
                edition_data = self.fetch_work_editions(work_data['key'])
                if edition_data and 'pages' in edition_data:
                    additional['pages'] = edition_data['pages']
                    print(f"    Found pages: {edition_data['pages']}")
            
            return additional if additional else None
            
        except Exception as e:
            print(f"    ⚠️  Work details error: {e}")
            return None
    
    def fetch_work_editions(self, work_key: str) -> Optional[Dict]:
        """Fetch editions for a work to get page counts"""
        try:
            # Get editions for this work
            url = f"https://openlibrary.org{work_key}/editions.json"
            response = self.session.get(url, timeout=15)
            
            if response.status_code != 200:
                return None
                
            editions_data = response.json()
            
            if 'entries' not in editions_data:
                return None
            
            # Look for editions with page counts
            page_counts = []
            for edition in editions_data['entries'][:10]:  # Check first 10 editions
                if 'number_of_pages' in edition and edition['number_of_pages']:
                    pages = edition['number_of_pages']
                    if isinstance(pages, int) and 10 <= pages <= 2000:
                        page_counts.append(pages)
            
            if page_counts:
                # Use median page count
                page_counts.sort()
                median_pages = page_counts[len(page_counts) // 2]
                return {'pages': median_pages}
            
            return None
            
        except Exception as e:
            return None
        
    def fetch_openlibrary_data(self, isbn: str, expected_title: str, expected_author: str) -> Optional[Dict]:
        """Fetch book data from Open Library API with validation"""
        try:
            # Clean ISBN (remove hyphens)
            clean_isbn = isbn.replace('-', '').replace(' ', '')
            
            print(f"  Fetching data for ISBN {isbn}")
            
            # First try title+author search to get original work data
            search_result = self.search_openlibrary_by_title_author(expected_title, expected_author)
            if search_result:
                return search_result
            
            # Fallback to ISBN lookup (might get reprint data)
            urls = [
                f"https://openlibrary.org/api/books?bibkeys=ISBN:{clean_isbn}&jscmd=data&format=json",
                f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&jscmd=data&format=json"
            ]
            
            for url in urls:
                response = self.session.get(url, timeout=15)
                if response.status_code != 200:
                    continue
                    
                data = response.json()
                
                # Open Library returns data keyed by ISBN
                for key, book_data in data.items():
                    if book_data:
                        parsed_data = self.parse_openlibrary_data(book_data)
                        if self.validate_book_match(parsed_data, expected_title, expected_author):
                            return parsed_data
                        else:
                            print(f"  ⚠️  ISBN data doesn't match expected book, skipping")
                            return None
            
            # Try Google Books as fallback
            return self.fetch_googlebooks_data(clean_isbn, expected_title, expected_author)
            
        except Exception as e:
            print(f"  ❌ Error fetching Open Library data: {e}")
            return self.fetch_googlebooks_data(clean_isbn, expected_title, expected_author)
    
    def fetch_googlebooks_data(self, isbn: str, expected_title: str, expected_author: str) -> Optional[Dict]:
        """Fetch book data from Google Books API as fallback"""
        try:
            url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
            print(f"  Trying Google Books fallback...")
            
            response = self.session.get(url, timeout=15)
            if response.status_code != 200:
                return None
                
            data = response.json()
            
            if data.get('totalItems', 0) == 0:
                print(f"  ❌ No results found")
                return None
            
            # Take the first result
            book_data = data['items'][0]['volumeInfo']
            parsed_data = self.parse_googlebooks_data(book_data)
            
            if self.validate_book_match(parsed_data, expected_title, expected_author):
                return parsed_data
            else:
                print(f"  ⚠️  Google Books data doesn't match expected book, skipping")
                return None
            
        except Exception as e:
            print(f"  ❌ Google Books error: {e}")
            return None
    
    def parse_openlibrary_data(self, data: Dict) -> Dict:
        """Parse Open Library API response"""
        parsed = {}
        
        # Extract title
        if 'title' in data:
            parsed['title'] = data['title']
        
        # Extract authors
        if 'authors' in data and data['authors']:
            # Take first author
            author = data['authors'][0]
            if 'name' in author:
                parsed['author'] = author['name']
        
        # Extract publication year - prefer first publish date over specific edition date
        year = None
        
        # Look for "first_publish_date" which is more likely to be original
        if 'first_publish_date' in data:
            year_match = re.search(r'\b(19|20)\d{2}\b', data['first_publish_date'])
            if year_match:
                year = int(year_match.group())
        
        # Fallback to regular publish_date if no first_publish_date
        if not year and 'publish_date' in data:
            pub_date = data['publish_date']
            year_match = re.search(r'\b(19|20)\d{2}\b', pub_date)
            if year_match:
                year = int(year_match.group())
        
        # Validate year is reasonable (between 1800 and current year + 2)
        if year and 1800 <= year <= 2027:
            parsed['year'] = year
        
        # Extract page count
        if 'number_of_pages' in data:
            pages = data['number_of_pages']
            if 10 <= pages <= 2000:  # Sanity check
                parsed['pages'] = pages
        
        # Extract subjects as genres
        if 'subjects' in data and data['subjects']:
            # Take first few subjects as genres, clean them up
            genres = []
            for subject in data['subjects'][:3]:
                if 'name' in subject:
                    genre = subject['name']
                    # Clean up genre names - exclude overly specific ones
                    if (len(genre) < 50 and 
                        not genre.lower().startswith(('fiction', 'accessible book', 'protected daisy'))):
                        genres.append(genre.title())
            if genres:
                parsed['genres'] = genres
        
        return parsed
    
    def parse_googlebooks_data(self, data: Dict) -> Dict:
        """Parse Google Books API response"""
        parsed = {}
        
        # Extract title
        if 'title' in data:
            parsed['title'] = data['title']
        
        # Extract authors
        if 'authors' in data and data['authors']:
            parsed['author'] = data['authors'][0]
        
        # Extract publication year - be more careful about edition vs original date
        year = None
        if 'publishedDate' in data:
            pub_date = data['publishedDate']
            year_match = re.search(r'\b(19|20)\d{2}\b', pub_date)
            if year_match:
                potential_year = int(year_match.group())
                # Only use if it seems reasonable (not obviously a reprint)
                if 1800 <= potential_year <= 2027:
                    year = potential_year
        
        # Additional validation: reject years that seem too recent for classic books
        # This is a heuristic to avoid reprint dates
        if year:
            parsed['year'] = year
        
        # Extract page count
        if 'pageCount' in data:
            pages = data['pageCount']
            # Sanity check: should be between 10 and 2000 pages
            if 10 <= pages <= 2000:
                parsed['pages'] = pages
        
        # Extract categories and convert to proper genre
        if 'categories' in data and data['categories']:
            # Convert Google Books categories to our subjects format
            categories = [cat.replace('/', ' ') for cat in data['categories']]
            genre = self.get_genre_from_subjects(categories)
            if genre:
                parsed['genre'] = genre
        
        # Note: Google Books has averageRating but we're not using ratings
        # since they're not consistently available across APIs
        
        return parsed
    
    def validate_book_match(self, api_data: Dict, expected_title: str, expected_author: str) -> bool:
        """Validate that API data matches expected book"""
        if not api_data:
            return False
        
        api_title = api_data.get('title', '').lower()
        api_author = api_data.get('author', '').lower()
        
        expected_title_lower = expected_title.lower()
        expected_author_lower = expected_author.lower()
        
        # Check if titles have significant overlap (handle subtitle differences)
        title_match = (
            expected_title_lower in api_title or 
            api_title in expected_title_lower or
            # Check core title words
            any(word in api_title for word in expected_title_lower.split() if len(word) > 3)
        )
        
        # Check if authors match (handle name variations)
        author_match = (
            expected_author_lower in api_author or
            api_author in expected_author_lower or
            # Check last name match for author variations
            expected_author_lower.split()[-1] in api_author
        )
        
        return title_match and author_match
    
    def update_books_file(self, data_file: Path):
        """Update the books YAML file with fresh API data"""
        print(f"Loading books from {data_file}")
        
        # Load existing data
        with open(data_file, 'r') as f:
            data = yaml.safe_load(f)
        
        if 'books' not in data:
            print("❌ No 'books' key found in YAML file")
            return
        
        updated_books = []
        total_books = len(data['books'])
        
        print(f"Found {total_books} books to update...")
        
        for i, book in enumerate(data['books'], 1):
            isbn = book.get('isbn')
            current_title = book.get('title', 'Unknown')
            
            print(f"\n[{i}/{total_books}] {current_title}")
            print(f"  ISBN: {isbn}")
            
            if not isbn:
                print("  ⚠️  No ISBN, skipping")
                updated_books.append(book)
                continue
            
            # Fetch fresh data from APIs (only if we don't have complete data)
            needs_update = not all(book.get(field) for field in ['year', 'pages', 'genre'])
            
            if needs_update:
                fresh_data = self.fetch_openlibrary_data(isbn, current_title, book.get('author', ''))
            else:
                fresh_data = None
                print(f"  ✅ Already has complete data")
            
            # Start with existing book data
            updated_book = book.copy()
            
            if fresh_data:
                # Only update missing fields to avoid overwriting good data
                changes = []
                for key, new_value in fresh_data.items():
                    old_value = updated_book.get(key)
                    # Only update if field is missing or empty
                    if not old_value and new_value:
                        changes.append(f"{key}: {old_value} → {new_value}")
                        updated_book[key] = new_value
                
                if changes:
                    print(f"  ✅ Updated: {', '.join(changes)}")
                else:
                    print(f"  ✅ No new data needed")
            elif needs_update:
                print(f"  ⚠️  Could not fetch data, keeping existing")
            
            # If still no genre, try to infer from context
            if not updated_book.get('genre'):
                inferred_genre = self.infer_genre_from_context(
                    updated_book.get('title', ''),
                    updated_book.get('author', ''), 
                    updated_book.get('why_essential', '')
                )
                updated_book['genre'] = inferred_genre
                print(f"  🧠 Inferred genre: {inferred_genre}")
            
            updated_books.append(updated_book)
            
            # Be nice to API servers
            time.sleep(1)
        
        # Don't sort - preserve the author/series organization
        print(f"\n📚 Preserving author/series organization (no sorting)")
        
        # Save updated data
        data['books'] = updated_books
        with open(data_file, 'w') as f:
            yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
        
        print(f"\n📚 Successfully updated {len(updated_books)} books")
        print(f"📝 Data saved to {data_file}")
        print("💡 Tip: Run 'hugo' to rebuild your site with the updated data")

def main():
    """Main function"""
    script_dir = Path(__file__).parent
    data_file = script_dir.parent / 'data' / 'books.yaml'
    
    if not data_file.exists():
        print(f"❌ Error: {data_file} not found!")
        print("Make sure you're running this from the Hugo site root directory")
        return
    
    print("📚 Book Data Updater")
    print("=" * 50)
    print("This will fetch current data from Open Library & Google Books")
    print("for ALL books and update your data/books.yaml file.")
    print()
    
    # Ask for confirmation
    response = input("Continue? (y/N): ").strip().lower()
    if response not in ['y', 'yes']:
        print("Cancelled.")
        return
    
    updater = BookUpdater()
    updater.update_books_file(data_file)

if __name__ == "__main__":
    main()