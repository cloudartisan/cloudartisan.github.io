Verify all project thumbnails exist and have the correct dimensions.

Please:
1. Use GlobTool to find all project directories in content/projects/
2. For each project:
   - Check if index.md exists
   - Extract thumbnail filename from front matter
   - Verify thumbnail file exists in the project directory
   - Check thumbnail dimensions (should be square 1:1 aspect ratio, ideally 512x512px)
   - Verify the image format is appropriate (PNG with transparency or SVG preferred for logos)
3. Report:
   - Projects with missing thumbnails
   - Projects with thumbnails that don't meet dimension requirements
   - Projects with thumbnails in non-optimal formats
   - Suggestions for fixing any issues found

This ensures all projects have properly formatted thumbnails for the project showcase.