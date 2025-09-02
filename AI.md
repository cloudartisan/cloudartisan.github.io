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
- Date format: YYYY-MM-DD in front matter (site timezone is Australia/Sydney)
- Use Hugo shortcodes for complex content elements
- Maintain responsive image usage with appropriate dimensions
- Always use UK English

## Timezone Configuration
- Site timezone: Australia/Sydney (set in config.yaml)
- Build process includes --buildFuture flag to handle timezone differences
- When creating new posts, use current date in Australia/Sydney timezone

## Writing Tone and Style
- Reference STYLE_GUIDE.md for comprehensive tone and voice guidelines
- Use personal, conversational tone rather than formal documentation style
- Write from first-person experience ("In my testing" not "In testing")
- Use personal recommendations ("I'd recommend" not "It is recommended")
- Share personal reactions and impressions ("I'm really impressed" not "This represents")
- Make it feel like sharing experiences with a colleague

### Examples of Personal vs Formal Tone:
- ❌ "The global installation proved more reliable in testing"
- ✅ "The global installation was much more reliable in my testing"

- ❌ "Having used both Claude Code and OpenAI's Codex CLI, here's how Gemini CLI differentiates itself"
- ✅ "I've been using both Claude Code and OpenAI's Codex CLI, so here's how Gemini CLI feels different"

- ❌ "I'd be interested to hear about your experiences"
- ✅ "I'd love to hear about your experiences"

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

## Pull Request Workflow
- For significant changes, create a feature branch and PR instead of pushing directly to main
- The PR validation workflow will automatically test:
  - Hugo build success (both development and production)
  - Content validation (front matter, required fields)
  - Internal link checking
  - Image reference validation
- All validation checks must pass before merging
- Use PR workflow for:
  - New blog posts (for review and validation)
  - Theme or configuration changes
  - Multiple file changes
  - Experimental features
