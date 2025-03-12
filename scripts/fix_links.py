#!/usr/bin/env python3
import os
import re
import glob
from datetime import datetime
import csv

def replace_broken_links(content, replacements):
    """Replace broken links based on the replacements dictionary."""
    for old_url, new_url in replacements.items():
        content = content.replace(old_url, new_url)
    return content

def fix_links_in_file(file_path, replacements):
    """Fix broken links in a file based on the replacements mapping."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract post date from filename or frontmatter
    date_match = re.search(r'(\d{4})-(\d{2})-(\d{2})', file_path)
    post_date = None
    if date_match:
        post_date = datetime.strptime(date_match.group(0), '%Y-%m-%d')
    else:
        # Try to get date from frontmatter
        date_match = re.search(r'date:\s*(\d{4}-\d{2}-\d{2})', content)
        if date_match:
            post_date = datetime.strptime(date_match.group(1), '%Y-%m-%d')
    
    # Save the original content for comparison
    original_content = content
    
    # Apply link replacements
    updated_content = replace_broken_links(content, replacements)
    
    # Write the updated content if changes were made
    if updated_content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        return True
    
    return False

def main():
    # Dictionary of known replacements
    # Format: 'old_url': 'new_url'
    replacements = {
        # Google App Engine links
        'http://code.google.com/appengine/downloads.html': 'https://cloud.google.com/appengine/docs/legacy/standard/python/download',
        'http://code.google.com/p/googleappengine/issues/': 'https://github.com/GoogleCloudPlatform/appengine-python-standard',
        'http://code.google.com/appengine/': 'https://cloud.google.com/appengine/docs/legacy',
        
        # AWS documentation
        'http://aws.amazon.com/developertools/AWS-Identity-and-Access-Management/4143': 'https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_tools.html',
        
        # Cloud Security Alliance links
        'http://www.cloudsecurityalliance.org/About.html': 'https://cloudsecurityalliance.org/about/',
        'http://www.cloudsecurityalliance.org/Research.html': 'https://cloudsecurityalliance.org/research/',
        'http://www.cloudsecurityalliance.org/guidance.html': 'https://cloudsecurityalliance.org/research/guidance/',
        'http://www.cloudsecurityalliance.org/cm.html': 'https://cloudsecurityalliance.org/research/cloud-controls-matrix/',
        
        # CloudAudit links
        'http://cloudaudit.org/': 'https://cloudsecurityalliance.org/research/working-groups/cloudaudit/',
        'http://cloudaudit.org/page3/page3.html': 'https://cloudsecurityalliance.org/research/working-groups/cloudaudit/',
        'http://cloudaudit.org/page4/page4.html': 'https://cloudsecurityalliance.org/research/working-groups/cloudaudit/',
        
        # PHP documentation
        'http://www.php.net/manual/en/apc.configuration.php': 'https://www.php.net/manual/en/apc.configuration.php',
        
        # GitHub links - update to https
        'http://github.com/': 'https://github.com/',
        
        # Twitter links - update to https
        'http://twitter.com/davidltaylor': 'https://twitter.com/davidltaylor',
        
        # uWSGI links
        'http://projects.unbit.it/downloads/uwsgi-latest.tar.gz': 'https://projects.unbit.it/downloads/uwsgi-latest.tar.gz',
        
        # RightScale links
        'http://www.rightscale.com/': 'https://www.flexera.com/flexera-one/cloud-cost-optimization',
        'http://support.rightscale.com/': 'https://docs.flexera.com/',
        
        # CloudArtisan links (your own site)
        'http://www.cloudartisan.com/': 'https://cloudartisan.com/',
    }
    
    # Get all markdown files in the posts directory
    post_files = glob.glob('content/posts/*.md')
    
    # Process each file
    fixed_files = 0
    fixed_links = []
    
    for file_path in post_files:
        if fix_links_in_file(file_path, replacements):
            fixed_files += 1
            post_name = os.path.basename(file_path)
            fixed_links.append(f"Fixed links in {post_name}")
    
    print(f"Fixed links in {fixed_files} files")
    for message in fixed_links:
        print(message)

if __name__ == "__main__":
    main()