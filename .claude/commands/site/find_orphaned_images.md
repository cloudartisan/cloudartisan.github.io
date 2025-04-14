Find unused images in the static/images directory.

Please:
1. Use GlobTool to catalog all image files in the static/images directory
2. Use GrepTool to search through all content files (posts, projects, pages) for references to each image
3. For each image:
   - Check for direct references in markdown format: ![alt](/images/path)
   - Check for shortcode references: {{< figure src="/images/path" >}}
   - Check for CSS references: url('/images/path')
   - Check for HTML img tags: <img src="/images/path">
   - Check for relative paths in project directories: ![alt](image.jpg)
   - Check for thumbnail references in frontmatter: thumbnail: "thumbnail.png"
   - Check for other common reference patterns
4. Compile a list of images that appear to be unused
5. Organize results by:
   - Definitely unused (no references found)
   - Potentially unused (found in unusual patterns that might be false negatives)
6. Pay special attention to variant size images (*-150x150.png, *-300x*.png) that might be automatically generated thumbnails
7. Provide suggestions for cleanup (with caution about removing potentially used images)
8. For orphaned variant sizes, suggest commands to safely remove them

This helps maintain a clean static directory without unused assets.