#!/bin/bash
# Helper script to create a new blog post via PR workflow

set -e

# Check if post title is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 'Post Title Here'"
    echo "Example: $0 'My New Blog Post'"
    exit 1
fi

POST_TITLE="$1"
# Convert title to slug (lowercase, spaces to hyphens, remove special chars)
POST_SLUG=$(echo "$POST_TITLE" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9 ]//g' | sed 's/ \+/-/g')
CURRENT_DATE=$(date '+%Y-%m-%d')
BRANCH_NAME="post/$POST_SLUG"
FILENAME="content/posts/$CURRENT_DATE-$POST_SLUG.md"

echo "Creating new post PR..."
echo "Title: $POST_TITLE"
echo "Slug: $POST_SLUG" 
echo "Branch: $BRANCH_NAME"
echo "File: $FILENAME"
echo ""

# Create and switch to new branch
git checkout -b "$BRANCH_NAME"

# Create the post file
cat > "$FILENAME" << EOF
---
title: "$POST_TITLE"
date: $CURRENT_DATE
draft: true
description: ""
tags: []
categories: []
author: "david-taylor"
---

## Introduction

[Your post content here]

## Conclusion

[Wrap up your thoughts]
EOF

echo "Created new post file: $FILENAME"
echo ""
echo "Next steps:"
echo "1. Edit the post content in $FILENAME"
echo "2. Add tags, categories, and description"
echo "3. Set draft: false when ready"
echo "4. Commit your changes: git add . && git commit -m 'Add $POST_TITLE post'"
echo "5. Push and create PR: git push -u origin $BRANCH_NAME"
echo "6. The PR validation workflow will test your changes"
echo ""
echo "Opening the post file for editing..."

# Open the file in the default editor if available
if command -v code > /dev/null; then
    code "$FILENAME"
elif command -v nano > /dev/null; then
    nano "$FILENAME"
else
    echo "Edit $FILENAME with your preferred editor"
fi