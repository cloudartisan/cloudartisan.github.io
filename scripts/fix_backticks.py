#!/usr/bin/env python3
import os
import re
import glob

def fix_backticks_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Save the original for comparison
    original_content = content
    
    # Replace <code>text</code> with `text`
    content = re.sub(r'<code>([^<]+?)</code>', r'`\1`', content)
    
    # Only write the file if changes were made
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    
    return False

def main():
    # Get all markdown files in the posts directory
    post_files = glob.glob('content/posts/*.md')
    
    # Process each file
    changed_files = 0
    for file_path in post_files:
        if fix_backticks_in_file(file_path):
            print(f"Fixed backticks in {file_path}")
            changed_files += 1
    
    print(f"Fixed backticks in {changed_files} files")

if __name__ == "__main__":
    main()