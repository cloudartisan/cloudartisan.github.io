#!/usr/bin/env python3
import os
import re
import glob

def fix_twitter_links_in_file(file_path):
    """Fix Twitter links in a file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Save the original content for comparison
    original_content = content
    
    # Update Twitter links from http to https
    updated_content = re.sub(
        r'(http://twitter\.com/davidltaylor)',
        r'https://twitter.com/davidltaylor',
        content
    )
    
    # Write the updated content if changes were made
    if updated_content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        return True
    
    return False

def main():
    # Get all markdown files in the posts directory
    post_files = glob.glob('content/posts/*.md')
    
    # Process each file
    fixed_files = 0
    fixed_posts = []
    
    for file_path in post_files:
        if fix_twitter_links_in_file(file_path):
            fixed_files += 1
            post_name = os.path.basename(file_path)
            fixed_posts.append(post_name)
    
    print(f"Fixed Twitter links in {fixed_files} files")
    print("Posts with fixed Twitter links:")
    for post in fixed_posts:
        print(f"- {post}")

if __name__ == "__main__":
    main()