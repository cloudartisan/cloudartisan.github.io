#!/usr/bin/env python3
import os
import subprocess
import re
import yaml
from pathlib import Path

# Make sure content/posts directory exists
os.makedirs("content/posts", exist_ok=True)

# Get list of posts from main branch
result = subprocess.run(
    ["git", "ls-tree", "-r", "--name-only", "main", "--", "_posts/"],
    capture_output=True,
    text=True,
)

post_files = result.stdout.strip().split("\n")

for post_file in post_files:
    # Get post content from main branch
    result = subprocess.run(
        ["git", "show", f"main:{post_file}"], capture_output=True, text=True
    )
    content = result.stdout

    # Extract filename without extension
    filename = os.path.basename(post_file)
    
    # Extract date and slug from filename
    date_slug_match = re.match(r'(\d{4}-\d{2}-\d{2})-(.+)\.md', filename)
    post_date = date_slug_match.group(1) if date_slug_match else None
    post_slug = date_slug_match.group(2) if date_slug_match else None
    
    # Destination path
    dest_path = f"content/posts/{filename}"
    
    # Initialize front matter with default values
    front_matter = {
        "title": post_slug.replace("-", " ").title() if post_slug else filename,
        "date": post_date,
        "draft": "false",
        "slug": post_slug,
    }
    
    # Try to extract title from content
    title_match = re.search(r'^title:\s*(.+?)$', content, re.MULTILINE)
    if title_match:
        front_matter["title"] = title_match.group(1).strip()
    
    # Try to extract published date
    date_match = re.search(r'published:\s*(.+?)$', content, re.MULTILINE)
    if date_match and date_match.group(1).strip():
        front_matter["date"] = date_match.group(1).strip()
    
    # Try to extract tags
    tags_match = re.search(r'tags:\s*\[(.+?)\]', content, re.MULTILINE | re.DOTALL)
    if tags_match:
        tags_str = tags_match.group(1)
        tags = [tag.strip().strip("'\"") for tag in tags_str.split(",")]
        front_matter["tags"] = tags
    
    # Try to extract summary/description
    summary_match = re.search(r'summary:\s*(.+?)(?:\n\n|\n---)', content, re.MULTILINE | re.DOTALL)
    if summary_match:
        summary = summary_match.group(1).strip()
        if summary:
            front_matter["description"] = summary
    
    # Try to identify where the content actually starts
    # Look for two consecutive newlines after the metadata section
    content_start = 0
    metadata_section_end = re.search(r'(^---\n.+?\n---\n|\ntitle:.+?\n\n|\npublished:.+?\n\n)', content, re.DOTALL)
    if metadata_section_end:
        content_start = metadata_section_end.end()
    else:
        # If we can't find a clear end to the metadata, look for the first paragraph break
        first_para_match = re.search(r'\n\n', content)
        if first_para_match:
            content_start = first_para_match.start()
    
    # Extract post content, skipping the front matter
    post_content = content[content_start:].strip()
    
    # If we couldn't extract content properly, use a fallback approach
    if not post_content or len(post_content) < 50:
        # Try to find the first occurrence of a markdown header or paragraph
        content_match = re.search(r'(^#|\n#|\n\n)', content)
        if content_match:
            post_content = content[content_match.start():].strip()
    
    # Clean up the title
    if isinstance(front_matter["title"], str):
        # Remove quotes
        front_matter["title"] = front_matter["title"].strip('"\'')
        # Ensure proper quoting for YAML
        if ":" in front_matter["title"] or front_matter["title"].startswith("[") or front_matter["title"].startswith("&"):
            front_matter["title"] = f'"{front_matter["title"]}"'
    
    # Clean up the post content
    # Convert code blocks from :::language to ```language
    post_content = re.sub(r':::(\w+)', r'```\1', post_content)
    
    # Fix indented code blocks to use proper markdown fence
    post_content = re.sub(r'(\n\s{4}```\w+.*?)(\n\n)', r'\1\n```\2', post_content, flags=re.DOTALL)
    
    # Fix image links
    post_content = re.sub(
        r'\[\!\[([^\]]+)\]\(([^)]+)\)\]\(([^)]+)\)', 
        r'![\1](\3)', 
        post_content
    )
    
    # Create new Hugo-compatible content
    new_content = "---\n"
    for key, value in front_matter.items():
        if value is not None:
            if isinstance(value, list):
                value_str = str(value).replace("'", '"')
                new_content += f"{key}: {value_str}\n"
            else:
                new_content += f"{key}: {value}\n"
    new_content += "---\n\n"
    new_content += post_content.strip() + "\n"
    
    # Write the converted content
    with open(dest_path, "w") as f:
        f.write(new_content)
    
    print(f"Converted {post_file} -> {dest_path}")

print("Conversion complete!")