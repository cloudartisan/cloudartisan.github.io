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

## Learning About Custom Slash Commands

I've been using Claude Code quite a bit lately, especially for managing this website, and I kept finding myself typing the same instructions over and over. "Create a new post with today's date," "check this file for UK English," "start the Hugo server" – these repetitive tasks were begging for shortcuts.

That's when I discovered custom slash commands in Claude Code. Think of them as your personal shortcuts for common tasks. Instead of typing out detailed instructions each time, you can invoke them with a simple `/command` syntax. They've been a massive time-saver for me, and I thought I'd share how I'm using them.

In this first post of my "Claude Code Tips & Tricks" series, I'll share the custom slash commands I've created to help maintain this Hugo website. I'm all about practical solutions, so these are real commands I use daily.

## What I've Learned About Custom Slash Commands

Custom slash commands are essentially saved prompts that you can invoke with a simple `/commandname` syntax. They're stored as Markdown files in your project, which means they can be version-controlled and shared with others.

While exploring the [official documentation](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/tutorials?q=worktrees#create-custom-slash-commands), I found that Claude Code supports two types of commands:

- **Project-scoped commands**: Stored in your project's `.claude/commands/` directory and specific to that project
- **User-scoped commands**: Stored in your home directory's `~/.claude/commands/` folder and available across all projects

I've been focusing on project-scoped commands since I wanted to share them with anyone who might work on this site in the future.

## The Commands I've Created for This Website

I've created several custom commands that address common tasks when managing this Hugo site:

1. `/project:newpost` - Quickly create a new post with proper front matter
2. `/project:ukcheck` - Ensure my posts use UK English with proper grammar and acronym definitions
3. `/project:linkcheck` - Verify all links in a post are valid
4. `/project:preview` - Generate and serve the site locally with a clickable link to the current post
5. `/project:upgradecheck` - Check for updates to Hugo and the Congo theme

Here's how I've set them up:

## How Custom Slash Commands Work

Creating custom slash commands is surprisingly simple. You just create Markdown files in a special directory structure, and Claude Code automatically recognizes them as commands.

The system supports two scopes for commands:

1. **Project-scoped commands** are available only within a specific project
   - I store these in the `.claude/commands/` directory within this website's repository
   - When I want to use one, I type `/project:command_name`

2. **User-scoped commands** are available across all my projects
   - These would be stored in `~/.claude/commands/` on my system
   - I'd access them with `/user:command_name`

I'm sticking with project-scoped commands for now since they can be checked into Git and shared with anyone who might help maintain this site.

### How Command Files Work

Each command is just a Markdown file that contains the instructions I want Claude to execute. The filename (minus the `.md` extension) becomes the command name.

So when I create:
- `.claude/commands/newpost.md`, I can invoke it with `/project:newpost`
- If I wanted subdirectories like `.claude/commands/posts/new.md`, I'd call it with `/project:posts:new`

What I really like is the ability to include placeholders using `$ARGUMENTS` syntax. This lets me pass in different values each time I use the command.

Here's the first command I created:

### My Post Creation Command: `/project:newpost`

My first and most-used command automates creating new posts. I created a file at `.claude/commands/newpost.md` with:

```markdown
I want to create a new blog post with the following details:

Title: $ARGUMENTS
Description: A description for the post

Please:
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

Now whenever I want to create a new post, I just type `/project:newpost My Amazing New Post` and Claude handles all the file creation with the right format and front matter. It's saved me countless minutes of repetitive work.

### UK English Checker: `/project:ukcheck`

A peculiar challenge I face is ensuring consistent UK English spelling in my posts (not US English). I created `.claude/commands/ukcheck.md`:

```markdown
Please review the file(s) $ARGUMENTS for:
1. UK English spelling (not US English)
2. Grammar and punctuation errors
3. Undefined acronyms - ensure each acronym is expanded on first use
4. Consistency in terminology and style

For each issue found, please provide:
- The location (file and approximate position)
- The current text
- The suggested correction
- A brief explanation when helpful

Use the View tool to read the files, then provide a summary of findings and suggested edits.
```

This command catches those sneaky "z" spellings that creep in and ensures I define acronyms properly.

### Link Validation: `/project:linkcheck`

After having a few embarrassing broken links in past posts, I created a link checker at `.claude/commands/linkcheck.md`:

```markdown
Please check all links in the file(s) $ARGUMENTS for validity:

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

### Local Preview: `/project:preview`

This is probably my second-most-used command, since I'm constantly previewing changes. It's stored in `.claude/commands/preview.md`:

```markdown
I want to preview the current Hugo site locally. Please:

1. Stop any running Hugo server processes
2. Serve the site with draft content enabled: `hugo server -D`
3. Provide the local URL where I can view the site
4. If I'm working on a specific post ($ARGUMENTS), give me the direct URL to that post so I can click it

Format the URL as a clickable link for easy navigation.
```

I love that it formats the URL as a clickable link so I can just click straight through to the post I'm working on.

### Theme Update Checker: `/project:upgradecheck`

Finally, I created a command to help me keep the site up-to-date at `.claude/commands/upgradecheck.md`:

```markdown
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
```

## Version Control Benefits

One of my favorite aspects of these commands is that they're just regular Markdown files in the project's directory structure. This brings several advantages:

1. They're automatically version-controlled with the rest of the site
2. Anyone who clones the repo gets all my custom commands for free
3. I can refine them over time with my normal Git workflow
4. If I mess something up, I have a history to roll back to

All I had to do was commit the `.claude/commands/` directory to my repository like any other files.

## Using My Custom Commands

Here's a quick summary of how I use these commands day-to-day:

1. When I want to write a new post:
   ```
   /project:newpost My Amazing New Post
   ```

2. When I want to make sure I'm using UK English (my American spelling has a tendency to creep in):
   ```
   /project:ukcheck content/posts/2025-04-14-claude-code-tips-slash-commands.md
   ```

3. Before publishing, I check all the links:
   ```
   /project:linkcheck content/posts/2025-04-14-claude-code-tips-slash-commands.md
   ```

4. To preview the site while I'm working:
   ```
   /project:preview content/posts/2025-04-14-claude-code-tips-slash-commands.md
   ```

5. Occasionally, to check if I need to update the theme or Hugo itself:
   ```
   /project:upgradecheck
   ```

One thing to remember is that `$ARGUMENTS` captures everything after the command name. So for commands that need complex input, I sometimes include instructions in the command itself about how to format the input.

## Other Command Ideas I'm Considering

I've just started exploring the possibilities, but here are some additional command ideas I'm considering:

- `/project:imageoptimize` - To automatically optimize images for a post (this would be amazing given my terrible track record with optimizing images)
- `/project:seo` - To analyze a post for SEO opportunities 
- `/project:stats` - To generate statistics about my blog (word count, post frequency, etc.)

## Organization Tips for Command Fanatics

As I create more commands, I'm starting to think about organizing them into subdirectories. If you end up with lots of commands, you might want to try something like this:

```
.claude/commands/
├── posts/
│   ├── new.md        # /project:posts:new
│   ├── check.md      # /project:posts:check
│   └── publish.md    # /project:posts:publish
├── site/
│   ├── preview.md    # /project:site:preview
│   └── deploy.md     # /project:site:deploy
└── general/
    └── help.md       # /project:general:help
```

This creates namespaced commands that help keep things organized. I haven't needed this level of organization yet, but it's nice to know it's available.

## Advanced Usage Tip: Documentation

I've also created a help command at `.claude/commands/help.md`:

```markdown
Here are all the available project commands:

- `/project:newpost` - Create a new blog post with proper front matter
- `/project:ukcheck` - Check posts for UK English spelling and grammar
- `/project:linkcheck` - Verify all links in posts are valid
- `/project:preview` - Generate and serve the site locally
- `/project:upgradecheck` - Check for updates to Hugo and the Congo theme

To get more details about a specific command, look at the corresponding Markdown file in the `.claude/commands/` directory.
```

This way, when I come back to this project after working on something else for a while, I can just type `/project:help` to get a refresher on what commands are available.

## Wrapping Up

I've found these custom slash commands to be huge time-savers in my workflow with Claude Code. They've eliminated repetitive tasks, ensured consistency in how I manage the site, and generally made working with Claude Code more efficient and enjoyable.

The beauty of this approach is that everything is stored as simple Markdown files in the project's `.claude/commands/` directory. This makes them easy to version control, share with others, and customize over time.

In future posts in this "Claude Code Tips & Tricks" series, I'll share more discoveries I've made while using Claude Code for various development tasks.

You can find all the commands I've mentioned in this post in the [GitHub repository for this website](https://github.com/cloudartisan/cloudartisan.github.io/tree/main/.claude/commands) if you want to use them as inspiration for your own custom commands.

If you create your own custom slash commands inspired by these, I'd be interested to hear about your experience. These commands have improved my workflow, and may prove useful for yours as well.

