# Cloud Artisan Site - Development Guide

## Development Philosophy
- This is a Hugo site - use idiomatic Hugo approaches for all changes where possible
- Prefer configuration changes over custom CSS/templates when available
- Follow the Congo theme conventions and documentation
- Use Hugo shortcodes instead of raw HTML when appropriate
- Keep customisations minimal and maintainable

## Project Status
- Profile image implemented at static/images/profile.png
- Site includes blog posts plus project showcase sections

## Deployment
- Target is GitHub Pages
- Domain is cloudartisan.com
- Repository is cloudartisan.github.io

## Build Commands
- Install Hugo: `go install -tags extended github.com/gohugoio/hugo@v0.145.0`
- Update theme modules: `hugo mod get -u`
- Local development: `hugo server -D` (includes draft content)
- Production build: `hugo` (generates static site in /public)
- Create new post: `hugo new content/posts/my-post-name.md`
- Create new project: `hugo new content/projects/project-name.md`

## Testing
- Preview site locally: `hugo server -D`
- Check links: `hugo server --navigateToChanged`

## Content Structure
- Posts: content/posts/
- Projects: content/projects/
- About: content/about/index.md
- Author info: content/authors/
- Homepage profile: content/_index.md

## Style Guidelines
- Use YAML for front matter in Markdown files
- Follow standard Markdown syntax
- File naming: Use kebab-case for filenames (e.g., my-post-name.md)
- Content organization: Place images in static/images/YYYY/MM/ folders
- Date format: YYYY-MM-DD in front matter
- Use Hugo shortcodes for complex content elements
- Maintain responsive image usage with appropriate dimensions
- Always use UK English

## Congo Theme Configuration
- Theme documentation: https://jpanther.github.io/congo/docs/
- Using Congo theme v2 (via git module)
- Configuration in config.yaml
- Use theme parameters in config.yaml rather than custom CSS whenever possible
- Reference theme shortcodes documentation for content formatting

## Git Guidelines
- Don't use emojis in commit messages
- Use clear, concise commit messages describing the changes
- Consolidate all changes for a single post into one commit
- Work locally until a post is completely ready before pushing
- Remember that pushing to main triggers the GitHub Pages deployment workflow
  and updates the site
