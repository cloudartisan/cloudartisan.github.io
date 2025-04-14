Verify all image references in the post(s) $ARGUMENTS exist in the filesystem.

Please:
1. Use the View tool to read the specified post(s)
2. Extract all image references (both Markdown format ![alt](path) and Hugo shortcode format {{< figure src="path" >}})
3. For each image reference:
   - Check if the path is absolute or relative
   - If relative, convert to the correct absolute path (considering the static/ directory for standard references)
   - Use GlobTool to verify the image exists
4. Report:
   - Total number of image references found
   - Number of images successfully verified
   - List of any missing images with their references
   - Suggestions for fixing missing images

This ensures all images referenced in posts are available and prevents broken image links.