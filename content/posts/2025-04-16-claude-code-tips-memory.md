---
title: "Claude Code Tips & Tricks: Maximising Memory"
date: 2025-04-16T10:55:08+10:00
draft: false
description: "Learn how to leverage Claude Code's memory features to reduce wasted prompts, set guardrails, and improve efficiency across your projects"
tags: ["Claude", "Claude Code", "Tips", "CLI", "Memory", "AI Assistants"]
categories: ["Tutorials"]
series: ["Claude Code Tips & Tricks"]
author: "david-taylor"
---

## The Power of Memory in Claude Code

Having used Claude Code for a while now to help manage this website and other projects, I've come to appreciate how crucial its memory features are for productive work. In AI assistants like Claude, memory refers to the system's ability to retain information across interactions, which can significantly reduce repetitive instructions and improve continuity.

In this post, I'll share what I've learned about Claude Code's memory capabilities and how they can help you work more efficiently with less frustration.

## Understanding Memory Scopes in Claude Code

Claude Code offers different scopes of memory that determine where and how information is stored and accessed. Understanding these scopes helps you make strategic decisions about where to put different types of information:

### User Scope

User-level memory applies across all your projects and is stored in your `~/.claude` directory. This is perfect for:

- Personal preferences that apply to all your work
- Coding or writing style guidelines you always follow
- Security or maintenance practices you want to enforce

I use this scope to maintain consistent UK English across all my projects, even though I work with primarily US organisations.

### Project Scope

Project-level memory is specific to a single project repository and is stored in the project root directory as `CLAUDE.md`. This is ideal for:

- Project-specific conventions and requirements
- Team standards that everyone should follow
- Technical details about the project architecture

For this website, my project-scoped memory includes Hugo-specific conventions and build commands in [CLAUDE.md](https://github.com/cloudartisan/cloudartisan.github.io/blob/main/CLAUDE.md).

## Configuring Memory: The CLAUDE.md Files

The primary way to configure Claude Code's memory is through Markdown files:

- **User-scope**: `~/.claude/CLAUDE.md` for personal preferences
- **Project-scope**: `CLAUDE.md` in the project's root directory for project-specific guidelines

These files allow you to define how Claude Code should interact with you and your projects, setting expectations and guidelines that persist across sessions.

### My User-Scope Configuration

Here's an excerpt from my `~/.claude/CLAUDE.md` file that sets global preferences:

```markdown
# General Instructions

## Code and Commits
- Do not include emojis in commit messages
- No blank lines with whitespace unless required by file format

## Access Permissions
- I permit all access to https://en.wikipedia.org
- I permit all access to https://docs.anthropic.com

## Language and Style
- Always use UK English

## Accuracy
- Never fabricate results from API calls or tools
- If a tool isn't working, acknowledge the limitation
- When operations fail, provide the actual error message
```

This configuration ensures Claude Code consistently applies these preferences across all my projects, eliminating the need to repeat these instructions in every conversation.

### My Project-Scope Configuration

For this Hugo website, I have a project-specific [`CLAUDE.md`](https://github.com/cloudartisan/cloudartisan.github.io/blob/main/CLAUDE.md) that includes:

```markdown
# Cloud Artisan Site - Development Guide

## Development Philosophy
- This is a Hugo site - use idiomatic Hugo approaches
- Prefer configuration over custom CSS/templates
- Follow Congo theme conventions

## Build Commands
 - Install Hugo: `go install -tags extended github.com/gohugoio/hugo@v0.145.0`
- Local development: `hugo server -D` (includes draft content)
- Production build: `hugo` (generates static site in /public)
- Create new post: `hugo new content/posts/my-post-name.md`
```

This project-specific memory means I never have to explain how the site works or remind Claude Code about Hugo conventions each time I ask for help.

## Practical Benefits of Using Memory Effectively

### Reduced Prompting Overhead

Before I started using Claude Code's memory features properly, I found myself repeating the same instructions constantly:

1. "Use UK English spelling"
2. "Follow the Hugo conventions for this site"
3. "Make sure to run this command to test your changes"

Now, with properly configured memory files, I can simply ask Claude Code to create a new post or fix an issue without repeating these instructions every time. The instructions are always there, automatically applied to every interaction.

### Consistent Outputs

Memory ensures consistency across interactions. For example, because my memory specifies UK English, I no longer get a mix of UK and US spelling in generated filenames or frontmatter, such as tags. This consistency extends to coding styles, commit message formats, and other project conventions.

### More Focused Interactions

With baseline preferences and requirements stored in memory, my interactions with Claude Code can focus on the specific task at hand rather than establishing context over and over. This makes each session more productive and less frustrating.

## Memory vs. Slash Commands: When to Use Each

In my [previous post about slash commands](/posts/2025-04-14-claude-code-tips-slash-commands/), I discussed how to create custom commands for repetitive tasks. It's worth understanding when to use memory versus slash commands:

- **Use memory for**: Guidelines, preferences, and context that should be applied consistently across many different tasks
- **Use slash commands for**: Specific, repeatable procedures that follow a defined workflow

For example, my preference for UK English belongs in memory since it applies to all content generation, while my process for creating a new blog post is better as a slash command since it's a specific workflow I execute repeatedly.

## Real Examples of Memory in Action

### Example 1: Maintaining UK English

As someone who works with both UK and US organisations, I often find myself needing to switch between spelling conventions. By adding this to my user-level memory:

```markdown
## Language and Style
- Always use UK English
```

Every interaction with Claude Code now respects UK spelling without me having to specify it each time. When I generate content, terms like "colour" and "optimisation" are consistently used rather than the US misspellings 😉.

### Example 2: Development Guidelines

For my colour palette generator project, I use a project-specific `CLAUDE.md` with development guidelines:

```markdown
## Code Style
- Backend: PEP 8, Black formatter (100 char line limit)
- Frontend: ESLint with Prettier
- Imports: standard library → third-party → local modules
- Type annotations required for all Python functions
- React components: functional components with TypeScript
- Naming: snake_case (Python), camelCase (JS/TS)
```

Now, whenever I ask Claude Code to add features or fix bugs in this project, it automatically follows these coding standards without me having to specify them each time. For example, it knows to add type annotations to all Python functions and to organise imports according to the project's conventions.

### Example 3: Security Standards

For projects with specific security requirements, I've found it valuable to add guidelines like:

```markdown
## Security Standards
- All user input must be validated and sanitised
- Database queries must use parameterised statements
- API endpoints with sensitive data require authentication
- Never log sensitive information (passwords, tokens, etc.)
```

This ensures Claude Code considers security implications in every code modification without requiring explicit reminders each time.

## Advanced Memory Techniques

### Combining With Slash Commands

I've found that combining memory with slash commands creates a powerful workflow. Memory provides the consistent baseline, while slash commands handle specific tasks within that context.

For example, my slash command for creating new posts doesn't need to specify UK English since that's already in memory, but it does need to specify the particular format for Hugo posts.

### Using Memory for Project Onboarding

When bringing new team members onto a project, I've started creating comprehensive `CLAUDE.md` files that serve as onboarding documentation. This means the same document can:

1. Help human developers understand the project
2. Configure Claude Code to follow project conventions
3. Provide a single source of truth for project standards

This dual-purpose approach ensures humans and AI assistants are working from the same playbook.

### Leveraging MCP for Extended Memory

For more advanced memory capabilities, the Model Context Protocol (MCP) offers a dedicated server-memory implementation. As I mentioned in [my earlier post on MCP servers](/posts/2025-04-12-adding-mcp-servers-claude-code/), this can enable more sophisticated memory patterns:

```bash
# Register server-memory
claude mcp add-json server-memory --scope user '{
  "command": "uvx",
  "args": [
    "mcp-server-memory"
  ]
}'
```

With the server-memory MCP, Claude Code can store and retrieve knowledge in a more structured way, allowing for complex data relationships beyond what the basic CLAUDE.md files can support.

## Troubleshooting Memory Issues

### When Memory Seems to Be Ignored

Sometimes it might seem like Claude Code is ignoring instructions in your memory files. Common causes include:

1. **Conflicting instructions**: If your user and project memory files contain contradictory guidance, Claude Code may prioritise one over the other or attempt to reconcile them
2. **Overwridden by direct prompts**: Explicit instructions in your current conversation may override memory settings
3. **Memory file formatting**: Ensure your CLAUDE.md files use clear, direct instructions

I've found it helpful to use the `/debug` command in Claude Code to check which memory files are being loaded and how they're being interpreted.

### Refreshing Memory

If Claude Code seems to have "forgotten" instructions from your memory files, you can explicitly ask it to reload them:

```
Please refresh your memory from my CLAUDE.md files and confirm the key instructions you're following.
```

This can be especially useful after making changes to your memory files or when starting a new session after a long break.

## Other Memory Uses in Claude Code

Claude Code supports some interesting memory capabilities that aren't immediately obvious:

1. **Hierarchical directory-based memory** - Claude Code reads CLAUDE.md files recursively up the directory tree, meaning you can create specialised memory files in subdirectories for different parts of your project
2. **Local memory overrides** with CLAUDE.local.md (which shouldn't be checked into version control)

There are also capabilities I'd like to see more of in future releases:

1. **More structured hierarchical memory** with clearer precedence rules
2. **Memory scopes beyond user and project** (perhaps team or organisation levels)
3. **More interactive memory management** through the Claude Code interface

## Cost Efficiency Through Memory Usage

A key benefit I haven't yet mentioned is cost efficiency. Claude Code, like other AI assistants, can become expensive when there's a lot of back-and-forth clarification or correction needed. Each message consumes tokens, and those costs add up quickly.

By investing time in proper memory configuration:

1. You eliminate repetitive instructions that waste tokens
2. You reduce the need for corrective prompts ("No, I meant UK English...")
3. You ensure consistent output that meets your requirements the first time

This isn't just about convenience: it's about making each interaction with Claude Code as efficient and cost-effective as possible. While it's difficult to quantify exact savings, properly configured memory can substantially reduce the number of messages needed to complete tasks, directly translating to lower costs and faster results.

## Conclusion

Effective use of memory in Claude Code can dramatically improve your workflow by reducing repetition, ensuring consistency, and maintaining important context across sessions. By thoughtfully configuring both user and project-level memory, you can create a more efficient and pleasant experience.

The key takeaways:

1. Use user-scope memory for personal preferences that apply across all projects
2. Use project-scope memory for technical details and conventions specific to a project
3. Combine memory with slash commands for the most efficient workflow
4. Keep memory files clear, direct, and well-organised

I've found that investing time in properly configuring memory has paid off many times over in smoother interactions and more consistent outputs. If you're using Claude Code regularly, I highly recommend taking the time to set up your memory files thoughtfully.

For more on Claude Code features, check out the other posts in this series tagged with [Claude Code](/tags/claude-code/).

Cheers!

