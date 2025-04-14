---
title: "Claude Code Tips & Tricks: Custom Slash Commands"
date: 2025-04-14T15:18:37+10:00
draft: true
description: "Learn how to create custom slash commands in Claude Code to automate repetitive tasks and enhance your workflow when managing a Hugo website."
tags: ["Claude", "Claude Code", "Tips", "CLI", "Slash Commands", "Hugo"]
categories: ["Tutorials"]
series: ["Claude Code Tips & Tricks"]
author: "david-taylor"
---

# Claude Code Tips & Tricks: Custom Slash Commands

## Introduction

If you've been using Claude Code for a while, you've probably found yourself typing the same commands or instructions repeatedly. Whether it's starting a new blog post, checking for errors, or running local servers, these tasks follow predictable patterns.

What if you could create shortcuts for these common workflows? That's exactly what custom slash commands in Claude Code allow you to do. They're like reusable templates that you can invoke with a simple `/command` syntax to avoid repetitive typing and ensure consistency.

In this first post of my "Claude Code Tips & Tricks" series, I'll show you how to create custom slash commands specifically designed to help maintain this Hugo website. By the end, you'll have a set of powerful shortcuts that make website management faster and more reliable, and you'll understand how to adapt this approach for your own projects.

## What Are Custom Slash Commands?

Custom slash commands are personalized shortcuts you can create in Claude Code that execute predefined prompts or instructions. Think of them as command aliases or script templates that you can invoke with a simple `/commandname` syntax.

While Claude Code comes with several built-in slash commands (like `/help` or `/mcp`), the real power comes from creating your own commands tailored to your specific workflows.

According to the [official documentation](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/tutorials?q=worktrees#create-custom-slash-commands), custom slash commands can help you:

- Create reusable prompts for common tasks
- Maintain consistency in repetitive operations
- Share standardized workflows with your team
- Automate complex multi-step processes

## Setting Up Our Custom Website Management Commands

For this website, we'll create several custom commands that address common tasks when managing a Hugo site. We'll store these commands in version control so they can evolve with the website and be shared with collaborators.

Here are the custom commands we'll implement:

1. `/newpost` - Create a new post with proper front matter
2. `/ukcheck` - Ensure posts use UK English with proper grammar and defined acronyms
3. `/linkcheck` - Verify all links in a post are valid
4. `/preview` - Generate and serve the site locally with a clickable link to the current post
5. `/upgradecheck` - Check for updates to Hugo and the Congo theme

Let's build these one by one.

## Creating Your First Custom Slash Command

To create a custom slash command in Claude Code, you use the `/cmd` built-in command followed by the configuration for your custom command.

Here's the basic format:

```
/cmd add mynewcommand "Description of what this command does" <<EOF
Instructions or prompt template that will run when the command is invoked
EOF
```

The structure has three main parts:
- Command name (without the slash)
- Description (helps you remember what the command does)
- Template content (the actual instructions or prompt to execute)

Let's implement our first command.

### Command 1: Creating New Posts with `/newpost`

Our first command will automate the creation of new posts with the proper front matter. Here's how we'll implement it:

```
/cmd add newpost "Create a new Hugo post with proper front matter" <<EOF
I want to create a new blog post with the following details:

Title: {{title}}
Description: {{description}}

Please:
1. Generate the proper kebab-case filename with today's date (YYYY-MM-DD-title-slug.md)
2. Create the file with Hugo's 'hugo new content' command
3. Update the front matter to include:
   - The title properly formatted
   - Today's date
   - draft: true
   - The description
   - Author: david-taylor
   - Series: {{series if provided}}
   - Tags: {{tags if provided}}
4. Show me the command to serve the site locally so I can preview it

Ensure all formatting follows UK English standards.
EOF
```

When used, this command will prompt for the title, description, and optional series and tags information, then create a properly formatted new post file.

### Command 2: UK English and Grammar Check with `/ukcheck`

For ensuring our content maintains consistent UK English spelling and proper grammar:

```
/cmd add ukcheck "Check posts for UK English, grammar, and undefined acronyms" <<EOF
Please review the following post(s) for:
1. UK English spelling (not US English)
2. Grammar and punctuation errors
3. Undefined acronyms - ensure each acronym is expanded on first use
4. Consistency in terminology and style

Post paths: {{file paths}}

For each issue found, please provide:
- The location (file and approximate position)
- The current text
- The suggested correction
- A brief explanation when helpful

Use the View tool to read the files, then provide a summary of findings and suggested edits.
EOF
```

### Command 3: Link Checking with `/linkcheck`

To verify that all links in a post are valid:

```
/cmd add linkcheck "Verify all links in posts are valid" <<EOF
Please check all links in the following post(s) for validity:

Post paths: {{file paths}}

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
EOF
```

### Command 4: Local Preview with `/preview`

For generating and serving the site locally:

```
/cmd add preview "Generate and serve the site locally" <<EOF
I want to preview the current Hugo site locally. Please:

1. Stop any running Hugo server processes
2. Serve the site with draft content enabled: `hugo server -D`
3. Provide the local URL where I can view the site
4. If I'm working on a specific post ({{post path if provided}}), give me the direct URL to that post so I can click it

Format the URL as a clickable link for easy navigation.
EOF
```

### Command 5: Theme Update Check with `/upgradecheck`

For checking for updates to Hugo and the Congo theme:

```
/cmd add upgradecheck "Check for Hugo and Congo theme updates" <<EOF
Please check if updates are available for:

1. The Hugo version we're currently using
2. The Congo theme version we're currently using

For each:
- Determine the current version
- Check for the latest available version
- Advise if an update is recommended
- Suggest commands to perform the update safely
- If major version changes are available, note potential compatibility issues

Then run a test build to verify compatibility if updates are available.
EOF
```

## Storing Custom Commands in Version Control

To make these commands reusable and shareable, we'll create a `.claude-commands.json` file in the repository. This way, the commands can be version-controlled and referenced in documentation.

First, we'll examine how to export our commands:

```
/cmd export
```

Then we'll save the exported commands to a file in the repository.

## Using Our Custom Commands

Here's a quick guide on how to use each of the commands we've created:

1. `/newpost` - Use when starting a new blog post
   ```
   /newpost
   Title: My Amazing New Post
   Description: This post explores the wonders of custom commands
   Series: Claude Code Tips & Tricks
   Tags: claude, tips, commands
   ```

2. `/ukcheck` - Use to check UK English in posts you're working on
   ```
   /ukcheck
   File paths: content/posts/2025-04-14-claude-code-tips-slash-commands.md
   ```

3. `/linkcheck` - Verify links in your posts
   ```
   /linkcheck
   File paths: content/posts/2025-04-14-claude-code-tips-slash-commands.md
   ```

4. `/preview` - Preview the site locally
   ```
   /preview
   Post path: content/posts/2025-04-14-claude-code-tips-slash-commands.md
   ```

5. `/upgradecheck` - Check for updates
   ```
   /upgradecheck
   ```

## Extending and Customizing Commands

The beauty of custom slash commands is that you can extend and customize them for your specific needs. Here are some ideas for additional commands you might find useful:

- `/imageoptimize` - Automatically optimize images for a post
- `/seo` - Analyze a post for SEO opportunities
- `/deploy` - Trigger a manual deployment of the site
- `/stats` - Generate statistics about your blog (word count, post frequency, etc.)

## Conclusion

Custom slash commands are a powerful way to streamline your workflow when managing a Hugo website with Claude Code. By creating these five commands, we've automated common tasks, reduced the potential for errors, and made the content creation process more efficient.

In future posts in this "Claude Code Tips & Tricks" series, we'll explore more advanced techniques for leveraging Claude Code to enhance your development workflow.

Remember, you can find the commands we created in this post in our [GitHub repository](https://github.com/cloudartisan/cloudartisan.github.io/blob/{{current_commit_sha}}/.claude-commands.json) for reference and reuse.

What custom slash commands have you created? Let me know in the comments, and maybe we can feature them in a future post!

