Find unused images in the static/images directory.

Please:
1. Use GlobTool to catalog all image files in the static/images directory
2. Use GrepTool to search through all content files (posts, projects, pages) for references to each image
3. For each image:
   - Check for direct references in markdown format: ![alt](/images/path)
   - Check for shortcode references: {{< figure src="/images/path" >}}
   - Check for CSS references: url('/images/path')
   - Check for other common reference patterns
4. Compile a list of images that appear to be unused
5. Organize results by:
   - Definitely unused (no references found)
   - Potentially unused (found in unusual patterns that might be false negatives)
6. Provide suggestions for cleanup (with caution about removing potentially used images)

This helps maintain a clean static directory without unused assets.