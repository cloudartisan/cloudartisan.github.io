---
title: "Claude Code Tips & Tricks: Custom Slash Commands"
date: 2025-04-14T15:18:37+10:00
draft: false
description: "Learn how to create custom slash commands in Claude Code to automate repetitive tasks and enhance your workflow when managing a Hugo website."
tags: ["Claude", "Claude Code", "Tips", "CLI", "Slash Commands", "Hugo"]
categories: ["Tutorials"]
series: ["Claude Code Tips & Tricks"]
author: "david-taylor"
---

## The Power of Custom Slash Commands

I've been using Claude Code to help manage this website, and I kept finding myself typing similar instructions repeatedly: "Create a new draft post titled \<X\>," "Check this file for spelling, grammar, and UK English," "Clear the cache and start the server" in a very wordy way with a lot of back and forth — these repetitive tasks were begging to be streamlined.

That's when I discovered custom slash commands in Claude Code. Think of them as shortcuts for common tasks. Instead of typing detailed instructions each time, you can invoke them with a simple `/command_name` syntax. They've been a time-saver for me, and I thought I'd share how I'm using them.

I figured I'd start a "Claude Code Tips & Tricks" series and share the custom slash commands I've created to help maintain this website.

## Understanding Custom Slash Commands

Custom slash commands are essentially saved prompts that you can invoke with a simple `/command_name` syntax. They can be stored as Markdown files in your project, which means they can be version-controlled and shared with others.

Looking through the [official documentation](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/tutorials?q=worktrees#create-custom-slash-commands), I found that Claude Code supports two types of commands:

- **Project-scoped commands**: Stored in your project's `.claude/commands/` directory and specific to that project
- **User-scoped commands**: Stored in your home directory's `~/.claude/commands/` folder and available across all projects

I've been focusing on project-scoped commands since I wanted a way to share them easily with anyone else who might work on sites like this.

## How to Create Custom Slash Commands

Creating custom slash commands is surprisingly simple. You just create Markdown files in a special directory structure, and Claude Code automatically recognises them as commands.

The system supports two scopes for commands:

1. **Project-scoped commands** are available only within a specific project
   - I store these in the `.claude/commands/` directory within this website's repository
   - When I want to use one, I type `/project:command_name` or `/project:category:command_name` if organised in subdirectories

2. **User-scoped commands** are available across all my projects
   - These would be stored in `~/.claude/commands/` on my system
   - I'd access them with `/user:command_name`

I'm sticking with project-scoped commands for now since they can be checked into Git and easily shared with others.

### Command File Structure

Each command is just a Markdown file that contains the instructions I want Claude to execute. The filename (minus the `.md` extension) becomes the command name.

So when I create:
- `.claude/commands/newpost.md`, I can call it with `/project:newpost`
- or, if I use subdirectories like `.claude/commands/posts/new.md`, I can call it with `/project:posts:new`

Command files also support interpolation using `$ARGUMENTS` syntax. This lets me pass in different values each time I use the command.

## My Custom Commands for Hugo Site Management

I've created several custom commands that address common tasks when managing this Hugo site. I've chosen to use a consistent verb-noun naming format to make them more intuitive, organised into categories:

![Screenshot of Claude Code custom commands](/images/2025/04/screenshot_claude_custom_commands.png)


### Post Management Commands

#### Creating New Posts: `/project:posts:new`

My first and most-used command automates creating new posts. I created a file at `.claude/commands/posts/new.md` with:

```markdown
I want to create a new blog post with the following title: $ARGUMENTS

1. Generate the proper kebab-case filename with today's date (YYYY-MM-DD-title-slug.md)
2. Create the file with Hugo's 'hugo new content' command
3. Update the front matter to include:
   - The title properly formatted
   - Today's date
   - draft: true
   - The description
   - Author: david-taylor
4. Show me the command to serve the site locally so I can preview it

Ensure all formatting follows UK English standards.
```

Now whenever I want to create a new post, I just type `/project:posts:new My Amazing New Post` and Claude handles all the file creation with the right format and front matter.

#### Finding Draft Posts: `/project:posts:find_drafts`

To keep track of posts I'm still working on, I created a command that lists all draft posts:

```markdown
Find all draft posts in the content/posts directory.

1. Use GlobTool to find all post files in the content/posts directory
2. Use GrepTool to check each file for 'draft: true' in the front matter
3. Sort the results by modification date (most recent first)
4. Display the list of draft posts with:
   - Filename
   - Post title
   - Last modification date
   - Brief description if available

This helps keep track of which posts still need work before publication.
```

This gives me a quick overview of what's in my drafts folder and which posts need attention.

#### Checking for UK English: `/project:posts:check_language`

A peculiar challenge I face is ensuring consistent UK English spelling in my posts. I work for a US company, so US English tends to creep in. So I created `.claude/commands/posts/check_language.md`:

```markdown
Review the file(s): $ARGUMENTS

Check for:
1. UK English spelling (not US English)
2. Grammar and punctuation errors
3. Undefined acronyms - ensure each acronym is expanded on first use
   (Note: No need to expand commonly understood acronyms like AI, UI, URL, HTML, CSS, etc., 
   or acronyms that are part of brand/company names like OpenAI)
4. Consistency in terminology and style

For each issue found, please provide:
- The location (file and approximate position)
- The current text
- The suggested correction
- A brief explanation when helpful

Use the View tool to read the files, then provide a summary of findings and suggested edits.
```

This command catches those sneaky "z" spellings that creep in and ensures I define acronyms properly.

#### Verifying Images: `/project:posts:check_images`

After dealing with broken image references one too many times, I created this command:

```markdown
Verify all image references exist in the filesystem for post(s): $ARGUMENTS

1. Use the View tool to read the specified post(s)
2. Extract all image references (both Markdown format ![alt](path) and Hugo shortcode format)
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
```

This helps me catch missing images before publishing.

#### Viewing Recent Posts: `/project:posts:recent`

When I need to see what I've been working on lately:

```markdown
Show the most recent blog posts in the content/posts directory.

1. Use GlobTool to find all post files in the content/posts directory
2. Sort the results by file modification date (most recent first)
3. Display the $ARGUMENTS most recent posts (default to 5 if no number is provided)
4. For each post, show:
   - Post title
   - Publication date from front matter
   - Draft status
   - Brief description if available
   - Tags/categories
   - Last modification date

This provides a quick overview of recent content work.
```

#### Checking Links: `/project:posts:check_links`

After having a few embarrassing broken links in past posts, I created a link checker at `.claude/commands/posts/check_links.md`:

```markdown
Check all links for validity in the file(s): $ARGUMENTS

For each link:
1. Extract the URL
2. Use the WebFetchTool to check if the link is accessible
3. Verify the link target is relevant to the surrounding content

Provide a summary of:
- Total number of links checked
- Number of working links
- Number of broken or suspicious links
- For each broken link, suggest alternatives if possible

Use the View tool to read the files first.
```

#### Publishing Posts: `/project:posts:publish`

When a post is ready to go live:

```markdown
I want to publish the draft post: $ARGUMENTS

1. Use the View tool to read the current post
2. Change 'draft: true' to 'draft: false' in the front matter
3. Verify all images and links with appropriate tools
4. Perform a final check for UK English spelling and grammar
5. Stage the changes with git add
6. Commit the changes with a descriptive message
7. Push to GitHub

This automates the publishing workflow for new posts.
```

### Project Management Commands

#### Creating New Projects: `/project:projects:new`

For adding new projects to my portfolio section:

```markdown
Create a new project with the title: $ARGUMENTS

1. Generate the proper kebab-case directory name for the project (content/projects/project-slug/)
2. Create the directory structure with:
   - index.md (main content file with proper front matter)
   - An empty thumbnail.png placeholder (or recommend dimensions)
3. Update the front matter in index.md to include:
   - title: properly formatted
   - description: from input
   - draft: true
   - weight: next available weight value
   - links: section for website/github/etc (with placeholders)
   - tags: appropriate technology tags
   - thumbnail: "thumbnail.png"
4. Add placeholder sections in the content:
   - Overview
   - Features
   - Technologies Used
   - Challenges & Solutions
   - Screenshots/Demo (with image shortcode examples)
5. Remind me to add a proper thumbnail image (square 1:1 aspect ratio, ideally 512x512px PNG with transparency or SVG for logos) before publishing

This ensures all projects follow a consistent structure and formatting.
```

#### Verifying Project Thumbnails: `/project:projects:check_thumbnails`

To ensure my project showcase looks good:

```markdown
Verify all project thumbnails exist and have the correct dimensions.

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
```

### Site Management Commands

#### Local Preview: `/project:site:preview`

This is probably my second-most-used command, since I'm constantly previewing changes. It's stored in `.claude/commands/site/preview.md`:

```markdown
I want to preview the current Hugo site locally.

1. Stop any running Hugo server processes
2. If I'm working on a specific post ($ARGUMENTS), show the local URL the post will be available at so I can click it
3. Otherwise, show the local URL the site will be available at so I can click it
4. Serve the site with draft content enabled: `hugo server -D`

Format the URL as a clickable link for easy navigation.
```

I love that it formats the URL as a clickable link so I can just CMD+click straight through to the post I'm working on.

#### Finding Unused Images: `/project:site:find_orphaned_images`

To keep my site's static assets clean:

```markdown
Find unused images in the static/images directory.

1. Use GlobTool to catalog all image files in the static/images directory
2. Use GrepTool to search through all content files (posts, projects, pages) for references to each image
3. For each image:
   - Check for direct references in markdown format: ![alt](/images/path)
   - Check for shortcode references in Hugo format
   - Check for CSS references: url('/images/path')
   - Check for HTML img tags: <img src="/images/path">
   - Check for relative paths in project directories: ![alt](image.jpg)
   - Check for thumbnail references in frontmatter: thumbnail: "thumbnail.png"
   - Check for other common reference patterns
4. Compile a list of images that appear to be unused
5. Organise results by:
   - Definitely unused (no references found)
   - Potentially unused (found in unusual patterns that might be false negatives)
6. Pay special attention to variant size images (*-150x150.png, *-300x*.png) that might be automatically generated thumbnails
7. Provide suggestions for cleanup (with caution about removing potentially used images)
8. For orphaned variant sizes, suggest commands to safely remove them

This helps maintain a clean static directory without unused assets.
```

#### Theme Update Checker: `/project:site:check_updates`

I created a command to help me keep the site up-to-date at `.claude/commands/site/check_updates.md`:

```markdown
Check if updates are available for:

1. The Hugo version we're currently using
2. The Congo theme version we're currently using

For each:
- Determine the current version
- Check for the latest available version
- Advise if an update is recommended
- Suggest commands to perform the update safely
- If major version changes are available, note potential compatibility issues

Then run a test build to verify compatibility if updates are available.
```

#### Site Deployment: `/project:site:deploy`

When it's time to go live:

```markdown
Deploy the site to GitHub Pages.

1. Run a final build with `hugo` (no draft content)
2. Verify the build completed successfully
3. Clean up generated content
4. Stage all changes with git
5. Commit with a message describing the deployment
6. Push to GitHub to trigger the GitHub Pages deployment

Provide a confirmation when complete and estimate when the changes will be live.
```

## Command Documentation and Organisation

### Documenting Available Commands

I've also created a help command at `.claude/commands/view_commands.md`:

```markdown
Here are all the available project commands, organised by category:

## Post Management

- `/project:posts:new` - Create a new blog post with proper front matter
- `/project:posts:check_language` - Check posts for UK English spelling and grammar
- `/project:posts:check_links` - Verify all links in posts are valid
- `/project:posts:publish` - Publish a draft post and push changes to GitHub
- `/project:posts:find_drafts` - List all draft posts with their details
- `/project:posts:check_images` - Verify all image references exist in the filesystem
- `/project:posts:recent` - Show the most recent blog posts

## Project Management

- `/project:projects:new` - Create a new project with proper structure and frontmatter
- `/project:projects:check_thumbnails` - Verify all project thumbnails exist and have correct dimensions

## Site Management

- `/project:site:preview` - Generate and serve the site locally
- `/project:site:check_updates` - Check for updates to Hugo and the Congo theme
- `/project:site:deploy` - Deploy the site to GitHub Pages
- `/project:site:find_orphaned_images` - Find unused images in static folder

To get more details about a specific command, look at the corresponding Markdown file in the `.claude/commands/` directory.
```

This way, when I come back to this project after working on something else, I can just type `/project:view_commands` to get a refresher on what commands are available.

### Directory Organisation

I've organised my commands into subdirectories to keep them well-structured:

```
.claude/commands/
├── posts/
│   ├── new.md
│   ├── check_language.md
│   ├── check_links.md
│   ├── publish.md
│   ├── find_drafts.md
│   ├── check_images.md
│   └── recent.md
├── projects/
│   ├── new.md
│   └── check_thumbnails.md
├── site/
│   ├── preview.md
│   ├── check_updates.md
│   ├── deploy.md
│   └── find_orphaned_images.md
└── view_commands.md
```

This creates namespaced commands that help keep things organised as the number of commands grows. The categorisation makes it intuitive to find the right command for any task.

## Benefits of Version-Controlled Commands

One of my favorite aspects of these commands is that they're just regular Markdown files in the project's directory structure. This brings several advantages:

1. They're automatically version-controlled with the rest of the site
2. Anyone who clones the repo gets all my custom commands for free
3. I can refine them over time with my normal Git workflow
4. If I mess something up, I have a history to roll back to

All I had to do was commit the `.claude/commands/` directory to my repository like any other files.

## Daily Usage Examples

Here's how I use these commands in my daily workflow:

1. When I want to write a new post:
   ```
   /project:posts:new My Amazing New Post
   ```

2. When I'm checking my content for UK English:
   ```
   /project:posts:check_language content/posts/2025-04-14-claude-code-tips-slash-commands.md
   ```

3. To find out which drafts I still need to finish:
   ```
   /project:posts:find_drafts
   ```

4. To verify all my images exist:
   ```
   /project:posts:check_images content/posts/2025-04-14-claude-code-tips-slash-commands.md
   ```

5. Before publishing, I check all the links:
   ```
   /project:posts:check_links content/posts/2025-04-14-claude-code-tips-slash-commands.md
   ```

6. To preview the site while I'm working:
   ```
   /project:site:preview content/posts/2025-04-14-claude-code-tips-slash-commands.md
   ```

7. To identify unused images that could be removed:
   ```
   /project:site:find_orphaned_images
   ```

One thing to remember is that `$ARGUMENTS` captures everything after the command name. So for commands that need complex input, I sometimes include instructions in the command itself about how to format the input. I also try to structure the markdown in such a way that if `$ARGUMENTS` is not supplied the markdown still makes sense and seems to be written with no single file/argument in mind.

## Future

### Command Ideas

I've just started exploring the possibilities, but here are some additional command ideas I'm considering:

- `/project:posts:optimise_images` - To automatically optimise images for a post
- `/project:posts:analyse_seo` - To analyse a post for SEO opportunities 
- `/project:site:view_stats` - To generate statistics about my blog (word count, post frequency, etc.)

### MCP?

Model Context Protocol (MCP) supports prompts. It's starting to seem like a good idea to make a more generalised Hugo MCP server with prompts that work for Hugo sites, regardless of theme or content. That way others can get more benefit from the prompts, contribute to it, and it can be extended to include specific tools and resources. Also, it would mean the prompts can be used in clients other than Claude Code and Claude Desktop, such as Cursor, Windsurf, etc.

## Wrapping Up

I've found these custom slash commands to be huge time-savers in my workflow with Claude Code. They've eliminated repetitive tasks, ensured consistency in how I manage the site, and generally made working with Claude Code more efficient and enjoyable.

The beauty of this approach is that everything is stored as simple Markdown files in the project's `.claude/commands/` directory. This makes them easy to version control, share with others, and customise over time.

In future posts in this "Claude Code Tips & Tricks" series, I'll share more discoveries I've made while using Claude Code for various development tasks.

You can find all the commands I've mentioned in this post in the [GitHub repository for this website](https://github.com/cloudartisan/cloudartisan.github.io/tree/main/.claude/commands) if you want to use them as inspiration for your own custom commands.

If you create your own custom slash commands inspired by these, I'd be interested to hear about your experience. These commands have improved my workflow, and may prove useful for yours as well.

Cheers!
