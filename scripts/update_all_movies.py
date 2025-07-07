#!/usr/bin/env python3
"""
Complete movie data updater - fetches and verifies ALL movies from YAML file
Replaces both update_movie_data.py and verify_movie_data.py
"""

import requests
import yaml
import time
import re
from pathlib import Path
from bs4 import BeautifulSoup
from typing import Dict, Optional

class MovieUpdater:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        
    def fetch_imdb_data(self, imdb_id: str) -> Optional[Dict]:
        """Fetch movie data from IMDB page"""
        try:
            url = f"https://www.imdb.com/title/{imdb_id}/"
            print(f"  Fetching {url}")
            
            response = self.session.get(url, timeout=15)
            if response.status_code != 200:
                print(f"  ❌ HTTP {response.status_code}")
                return None
                
            soup = BeautifulSoup(response.text, 'html.parser')
            data = {}
            
            # Extract title (clean it up)
            title_elem = soup.find('h1', {'data-testid': 'hero__pageTitle'})
            if title_elem:
                title = title_elem.get_text(strip=True)
                # Remove year suffix if present
                title = re.sub(r'\s*\(\d{4}\).*$', '', title)
                data['title'] = title
            
            # Extract year
            year_elem = soup.find('a', href=re.compile(r'/year/\d+/'))
            if year_elem:
                year_match = re.search(r'(\d{4})', year_elem.get_text())
                if year_match:
                    data['year'] = int(year_match.group(1))
            
            # Extract IMDB rating
            rating_elem = soup.find('span', {'data-testid': 'rating-button__aggregate-rating__score'})
            if rating_elem:
                rating_text = rating_elem.get_text(strip=True)
                rating_match = re.search(r'(\d+\.?\d*)', rating_text)
                if rating_match:
                    data['imdb_rating'] = float(rating_match.group(1))
            
            # Extract runtime - look for duration patterns
            runtime = None
            
            # Try multiple selectors for runtime
            time_selectors = [
                'time',
                '[data-testid*="duration"]',
                '.runtime',
                '.titleDetails time'
            ]
            
            for selector in time_selectors:
                runtime_elem = soup.select_one(selector)
                if runtime_elem:
                    time_text = runtime_elem.get_text()
                    break
            else:
                # Look for duration patterns in page text
                time_text = soup.get_text()
            
            if time_text:
                # Look for patterns like "2h 49m", "149 min", "2 hr 29 min"
                patterns = [
                    r'(\d+)\s*h\s*(\d+)\s*m',  # "2h 49m"
                    r'(\d+)\s*hr\s*(\d+)\s*min',  # "2 hr 49 min" 
                    r'(\d+)\s*minutes?',  # "149 minutes"
                    r'(\d+)\s*mins?',     # "149 mins"
                ]
                
                for pattern in patterns:
                    match = re.search(pattern, time_text)
                    if match:
                        if len(match.groups()) == 2:  # hours and minutes
                            hours = int(match.group(1))
                            mins = int(match.group(2))
                            runtime = hours * 60 + mins
                        else:  # just minutes
                            runtime = int(match.group(1))
                        break
                
                # Sanity check: runtime should be between 5 and 300 minutes
                if runtime and 5 <= runtime <= 300:
                    data['runtime'] = runtime
            
            # Extract genres - be more selective
            genre_elems = soup.find_all('span', class_='ipc-chip__text')
            genres = []
            
            # List of valid genre categories
            valid_genres = {
                'Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 
                'Documentary', 'Drama', 'Family', 'Fantasy', 'Film-Noir', 'History',
                'Horror', 'Music', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 
                'Sport', 'Thriller', 'War', 'Western'
            }
            
            for elem in genre_elems:
                text = elem.get_text(strip=True)
                # Only include standard IMDB genres, filter out weird stuff
                if (text in valid_genres or 
                    (text and len(text) > 3 and len(text) < 20 and
                     not text.isdigit() and 
                     not re.match(r'\d+\.?\d*', text) and
                     text not in ['Top 250', 'Watchlist', 'Back to top', 'See full summary'])):
                    genres.append(text)
            
            # Take first 3 genres maximum, prefer standard ones
            standard_genres = [g for g in genres if g in valid_genres]
            other_genres = [g for g in genres if g not in valid_genres]
            
            final_genres = (standard_genres + other_genres)[:3]
            if final_genres:
                data['genres'] = final_genres
            
            # Extract director (first director link)
            # Look for director in credits section
            director_elem = soup.find('a', href=re.compile(r'/name/nm\d+/'))
            if director_elem:
                director_text = director_elem.get_text(strip=True)
                # Clean up director name
                if director_text and len(director_text) > 1:
                    data['director'] = director_text
            
            return data
            
        except Exception as e:
            print(f"  ❌ Error: {e}")
            return None
    
    def update_movies_file(self, data_file: Path):
        """Update the movies YAML file with fresh IMDB data"""
        print(f"Loading movies from {data_file}")
        
        # Load existing data
        with open(data_file, 'r') as f:
            data = yaml.safe_load(f)
        
        if 'movies' not in data:
            print("❌ No 'movies' key found in YAML file")
            return
        
        updated_movies = []
        total_movies = len(data['movies'])
        
        print(f"Found {total_movies} movies to update...")
        
        for i, movie in enumerate(data['movies'], 1):
            imdb_id = movie.get('imdb_id')
            current_title = movie.get('title', 'Unknown')
            
            print(f"\n[{i}/{total_movies}] {current_title} ({imdb_id})")
            
            if not imdb_id:
                print("  ⚠️  No IMDB ID, skipping")
                updated_movies.append(movie)
                continue
            
            # Fetch fresh data from IMDB
            fresh_data = self.fetch_imdb_data(imdb_id)
            
            # Start with existing movie data
            updated_movie = movie.copy()
            
            if fresh_data:
                # Show what we found
                changes = []
                for key, new_value in fresh_data.items():
                    old_value = updated_movie.get(key)
                    if old_value != new_value:
                        changes.append(f"{key}: {old_value} → {new_value}")
                        updated_movie[key] = new_value
                
                if changes:
                    print(f"  ✅ Updated: {', '.join(changes)}")
                else:
                    print(f"  ✅ Already up to date")
            else:
                print(f"  ⚠️  Could not fetch data, keeping existing")
            
            updated_movies.append(updated_movie)
            
            # Be nice to IMDB servers
            time.sleep(2)
        
        # Sort alphabetically by title
        updated_movies.sort(key=lambda x: x.get('title', '').upper())
        
        # Save updated data
        data['movies'] = updated_movies
        with open(data_file, 'w') as f:
            yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
        
        print(f"\n🎬 Successfully updated {len(updated_movies)} movies")
        print(f"📝 Data saved to {data_file}")
        print("\n💡 Tip: Run 'hugo' to rebuild your site with the updated data")

def main():
    """Main function"""
    script_dir = Path(__file__).parent
    data_file = script_dir.parent / 'data' / 'movies.yaml'
    
    if not data_file.exists():
        print(f"❌ Error: {data_file} not found!")
        print("Make sure you're running this from the Hugo site root directory")
        return
    
    print("🎬 Movie Data Updater")
    print("=" * 50)
    print("This will fetch current data from IMDB for ALL movies")
    print("and update your data/movies.yaml file.")
    print()
    
    # Ask for confirmation
    response = input("Continue? (y/N): ").strip().lower()
    if response not in ['y', 'yes']:
        print("Cancelled.")
        return
    
    updater = MovieUpdater()
    updater.update_movies_file(data_file)

if __name__ == "__main__":
    main()