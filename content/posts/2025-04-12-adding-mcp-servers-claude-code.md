---
title: "Setting Up Official MCP Servers with Claude Code"
date: 2025-04-12
draft: false
description: "How to install and configure official Model Context Protocol (MCP) servers to extend Claude Code's capabilities"
tags: ["AI", "Claude", "MCP", "CLI"]
---

## What Are MCP Servers?

MCP (Model Context Protocol) servers extend the capabilities of AI Assistants. These servers act as bridges to additional functionality by enabling AI Assistants to interact with external tools and services.

MCP servers can turn AI Assistants like Claude Desktop from a simple chat-based assistant into something more like Claude Code. Claude Code has the ability to fetch from allowed sites, interact with the filesystem, and use command-line tools such as git. That alone already makes Claude Code a handy development tool. However, Claude Code recently (about a month or so ago) also gained the ability to work with MCP servers. Now, Claude Code can be extended further, such as integrating with Stripe, Xero, Supabase, Blender, and more.

This post focuses on setting up the official reference MCP servers from the Model Context Protocol organisation. These won't make _much_ of a difference to the current functionality of Claude Code. That's not the point of this post. This post is here as a simple reference to show you how to get MCP servers working with Claude Code as a proof of concept, without the added complexity of configuring access tokens, Docker, and more.

For more details about the Model Context Protocol, have a look at the [official MCP website](https://modelcontextprotocol.io/) or the [MCP servers GitHub repository](https://github.com/modelcontextprotocol/servers).

## Why Use MCP Servers?

MCP servers enable Claude Code to:

- Use specialised development tools
- Access an array of APIs and SaaS
- Integrate with custom workflows
- Make use of reusable prompt templates

## Types of MCP Servers

There are many types of MCP servers available, each providing different capabilities.

The [official Model Context Protocol servers](https://github.com/modelcontextprotocol/servers) provide a standard set of capabilities:

**Basic Utility Servers:**
- `server-fetch`: For fetching content from URLs and web resources
- `server-time`: For accurate date and time operations
- `server-filesystem`: For working with files and directories

**Developer Tool Servers:**
- `server-git`: For advanced Git operations and version control
- `server-github`: For direct GitHub integration (repositories, issues, PRs)
- `server-code-interpreter`: For executing code in different languages
- `server-image`: For image manipulation and analysis

**Advanced Capability Servers:**
- `server-memory`: For persistent knowledge storage across sessions

We are going to set some of these up. Now, you might be thinking, "But, wait, Claude Code can already do some of that," and you'd be right. The point of this post isn't to make Claude Code into a genius-level 10X engineer, it's to demonstrate how you can customise your own Claude Code through examples with a few of the reference MCP servers.

## Setting Up MCP Servers

Setting up MCP servers with Claude Code is fairly simple:

The best way to use MCP servers depends on the specific server type and your use-case. For local development, an "stdio" server will do fine. And, if you don't want to mess with having many Docker containers running, most people will do fine with running them through `uvx` (for Python) or `npx` (for Node.js). For the purposes of this post we'll be sticking with local and simple.

To set up the reference MCP servers to run via `uvx` and `npx`, follow these steps:

1. First, register each MCP server using the Claude Code CLI:

```bash
# Install prerequisites on macOS:
brew install uv
brew install node

# Register server-time (date and time operations)
# IMPORTANT: Replace Australia/Sydney with your own timezone
claude mcp add-json server-time --scope user '{
  "command": "uvx",
  "args": [
    "mcp-server-time",
    "--local-timezone",
    "Australia/Sydney"
  ]
}'

# Register server-fetch (URL content fetching)
claude mcp add-json server-fetch --scope user '{
  "command": "uvx",
  "args": [
    "mcp-server-fetch"
  ]
}'

# Register server-git (git operations)
claude mcp add-json server-git --scope user '{
  "command": "uvx",
  "args": [
    "mcp-server-git"
  ]
}'

# Register server-filesystem (file operations)
# Note: Replace /path/to/allowed/directory with directories you want to grant access to
claude mcp add-json server-filesystem --scope user '{
  "command": "npx",
  "args": [
    "-y",
    "@modelcontextprotocol/server-filesystem",
    "/Users/your-username/Desktop",
    "/Users/your-username/Documents",
    "/Users/your-username/Downloads",
    "/Users/your-username/git"
  ]
}'
```

After registration, you can verify that the servers are properly configured:

```bash
claude mcp list
```

This should show all configured MCP servers:

![Screenshot of available MCP servers](/images/2025/04/screenshot_claude_avail_mcp_servers.png)

As shown in the screenshot, when registration is successful, you'll see all four official MCP servers listed.

> Notice that we use `uvx` for time, fetch, and git servers, while using `npx` for the filesystem server with explicit directory permissions. This is simply because they're written in different languages (Python and Node.js).

## MCP Configuration Approaches

While the CLI is handy for quick setup, understanding the underlying configuration gives you more control over your MCP server ecosystem. 

### Command-Line vs Direct Configuration

The `claude mcp` command offers several options for managing MCP servers:

- `add`: Interactive wizard to add a server
- `add-json`: Add a server using JSON configuration
- `list`: View all configured MCP servers
- `remove`: Delete an MCP server
- `get`: View details of a specific server

I prefer the `add-json` method as it's more scriptable and gives you a clearer picture of what's happening. The wizard is convenient but less flexible for complex setups.

### Configuration Scopes and Files

When adding MCP servers, you specify a scope using the `--scope` flag:

```bash
claude mcp add-json --scope=user server-name '{...configuration...}'
```

Available scopes include:

- `local` (default): Available only in your current session. These servers are temporary and will not persist when you close Claude Code.
- `user`: Available across all your projects on your system. This is stored in `~/.claude/mcp.json` and is my recommended choice for tools you'll use regularly.
- `project`: Available to anyone working on this specific project who has Claude Code installed. These settings are stored in the project's `.mcp.json` file, making them shareable with your team.

For personal tooling, the `user` scope is typically best as it reduces duplication and ensures consistent availability.

### Understanding Configuration Files

If you're curious about how Claude stores these configurations, take a look at the JSON files:

- `~/.claude.json` for user-scoped servers
- `.mcp.json` for project-scoped servers

These files contain the server definitions in a simple JSON structure, which you can edit directly if needed.

## Using MCP Servers with Claude Code

MCP servers are designed to extend Claude Code's capabilities through implicit usage. After installation, Claude should automatically detect when a query requires an MCP server's functionality and use it appropriately.

### MCP Server Integration Status

After installing MCP servers, you can verify they are registered in Claude's configuration:

```bash
claude mcp get server-time
```

This will show details about the server configuration:

```
server-time:
  Scope: User (available in all your projects)
  Type: stdio
  Command: uvx
  Args: mcp-server-time --local-timezone Australia/Sydney
```

### Verifying Your MCP Servers

You have several ways to verify your MCP servers are properly set up and connected:

1. **Check Configuration (Lists Registration Only)**:
   ```bash
   claude mcp list
   ```
   This shows registered servers but doesn't confirm they connect successfully.

2. **Check Connection Status (Shows Connection State)**:
   ```bash
   claude
   ```
   Then enter the command:
   ```
   /mcp
   ```
   This displays the connection status of each MCP server, showing either "connected" or "failed" for each one.

3. **Debug Connection Issues**:
   ```bash
   claude --mcp-debug
   ```
   This launches Claude with detailed MCP connection debugging information.
   
4. **Test with Natural Language**:
   Once launched, you can test specific MCP servers with natural language queries:
   
   * **Testing server-time**:
     ```
     What time is it now?
     What time is it in San Francisco?
     ```
     
     ![Screenshot of server-time MCP server in action](/images/2025/04/screenshot_claude_time.png)
     
     As shown in the screenshot, when the server-time MCP server is working correctly:
     - You can see the MCP function calls being made (green dots)
     - The raw JSON responses show timezone information
     - Claude provides a human-friendly response based on the raw response
     - You can query both current time and perform timezone conversions
     
   * **Testing server-filesystem**:
     ```
     What's the content of the README.md file?
     ```
     
   * **Testing server-git**:
     ```
     What are the recent commits in this repository?
     ```
     
   * **Testing server-fetch**:
     ```
     What's the latest news on Anthropic's website?
     ```
     
   * **General status**:
     ```
     What MCP servers do we have available?
     ```

5. **Check Connection Status in Claude**:
   When you run the `/mcp` command inside Claude Code, you'll see a status display like this:
   
   ```
   /mcp
     ⎿  MCP Server Status
     ⎿
     ⎿  • server-fetch: connected
     ⎿  • server-filesystem: connected
     ⎿  • server-git: connected
     ⎿  • server-time: connected
   ```

If any server shows "failed", refer to the troubleshooting steps in the section below.

6. **Test Individual Servers Directly**:
   You can verify each server works outside of Claude by testing it directly:
   
   * **Testing server-time**:
     ```bash
     uvx mcp-server-time --local-timezone Australia/Sydney --help
     ```
     
   * **Testing server-fetch**:
     ```bash
     uvx mcp-server-fetch --help
     ```
     
   * **Testing server-git**:
     ```bash
     uvx mcp-server-git --help
     ```
   
   If these commands show help information without errors, the packages are installed correctly.

### Integration Considerations

Keep in mind that MCP server integration with Claude Code is still developing. After installation, you might encounter:

1. **Connection Issues**: You might notice MCP servers failing to connect when starting Claude Code. Common causes include:
   - Registration command using incorrect configuration
   - Using npx with packages that aren't published to npm registry
   - Network issues blocking package downloads
   - Using the wrong approach for a particular server (npx vs uvx vs docker)
   - **Timezone problems**: The server-time server needs a valid IANA timezone (like "Australia/Sydney" or "Europe/London"), not an abbreviation (like "AEST" or "GMT")

2. **Troubleshooting Connection Issues**: If you see a message like "4 MCP servers failed to connect", the solution is to use the proper tools for each MCP server:

   - For time, fetch, and git servers: Use the `uvx` tool instead of `npx`
   - For filesystem server: Use `npx` with explicit directory paths
   
   The recommended setup is:
   ```bash
   # First install uv
   brew install uv  # macOS
   
   # Configure servers
   # IMPORTANT: Specify your IANA timezone (e.g., Europe/London, America/New_York)
   claude mcp add-json server-time --scope user '{
     "command": "uvx",
     "args": [
       "mcp-server-time",
       "--local-timezone",
       "Australia/Sydney"
     ]
   }'
   
   claude mcp add-json server-fetch --scope user '{
     "command": "uvx", 
     "args": ["mcp-server-fetch"]
   }'
   
   claude mcp add-json server-git --scope user '{
     "command": "uvx",
     "args": ["mcp-server-git"]
   }'
   
   claude mcp add-json server-filesystem --scope user '{
     "command": "npx",
     "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/directory"]
   }'
   ```
   
   For additional debugging:
   - Use the `--mcp-debug` flag when launching Claude Code:
     ```bash
     claude --mcp-debug
     ```
   - Check for error messages in the output when servers try to connect

3. **Limited Documentation**: The specific interaction patterns with each server may not be fully documented

4. **Implicit Usage**: Unlike explicit tool calls, MCP servers are designed to be used implicitly through natural language queries

The Model Context Protocol and its server implementations are still maturing, and the integration between the servers and Claude Code is likely to improve over time. For the most up-to-date information on using MCP servers with Claude Code, refer to the [official documentation](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/tutorials#set-up-model-context-protocol-mcp).

## Practical Example: Using MCP Servers Together

Let me show a practical example of how these servers can work together. Imagine you want to create project documentation that includes time information, fetches reference material, examines git history, and explores the filesystem.

Here's how a conversation with Claude might go:

```
You: I need to document our repository structure with historical context. What are the key directories and when were they created?

Claude: I'll help you document the repository structure with historical context.
[Claude uses server-filesystem to scan your project structure]
[Claude uses server-git to check when each directory was created]

The main directories in this repository are:
- src/ (created January 2025 by Alice)
- tests/ (created January 2025 by Bob)
- docs/ (created March 2025 by Charlie)
...

You: Add a section about best practices for our project structure.

Claude: [Uses server-fetch to get relevant documentation standards]
[Uses server-time to note when this documentation was created]

I've added a "Project Structure Best Practices" section that includes:
- Guidelines for organizing components
- Naming conventions for files and directories 
- References to industry standards
...
Documentation timestamp: April 12, 2025 14:30 AEST
```

The beauty of MCP servers is that Claude can seamlessly combine these capabilities without you having to explicitly request each tool. The conversation feels natural, but Claude is accessing far more contextual information than would be possible otherwise.

## Alternative MCP Servers

If the official MCP servers from the Model Context Protocol organization aren't available yet, there are alternatives you can use. Here are a few community-developed MCP servers available on npm:

1. **General-purpose Servers**
   - `@wonderwhy-er/desktop-commander`: Provides terminal operations and file editing
   - `@anaisbetts/mcp-installer`: A meta-server that helps install other MCP servers
   - `@smithery/cli`: A command for installing and listing MCP servers

2. **Special-purpose Servers**
   - `tavily-mcp`: Advanced web search capabilities
   - `@openbnb/mcp-server-airbnb`: Airbnb search and listing details
   - `mcp-obsidian`: Integration with Obsidian knowledge base
   - `@executeautomation/playwright-mcp-server`: Automation testing with Playwright

You can find these by searching npm:

```bash
npm search mcp
```

To add an alternative server, follow the same pattern as the official servers:

```bash
# Example for adding the desktop-commander server
claude mcp add-json desktop-commander --scope user '{
  "command": "npx",
  "args": [
    "@wonderwhy-er/desktop-commander@latest"
  ]
}'
```

When choosing alternative servers, pay special attention to security considerations and verify the reputation of the package maintainers.

## Security Considerations

### Trust and Permissions

Always review MCP server configurations before adding them, especially from third-party sources. MCP servers execute commands on your system, so ensure you trust their source and understand what they're doing.

When using MCP servers that require authentication (like GitHub tokens), follow these security practices:
- Use tokens with the minimum necessary permissions
- Set appropriate expiration dates
- Never share tokens in public forums or commit them to repositories
- Revoke tokens immediately if accidentally exposed

### Using Environment Variables for Credentials

For MCP servers that need access tokens or API keys, it's better to use environment variables rather than hardcoding credentials. Here's an example of configuring a server with environment-based authentication:

```bash
claude mcp add-json api-server --scope user '{
  "command": "npx",
  "args": [
    "@acme/api-server"
  ],
  "env": {
    "API_KEY": "${API_KEY}"
  }
}'
```

Then when launching Claude, provide the variable:

```bash
API_KEY=your_actual_key_here claude
```

This approach keeps sensitive values out of configuration files and reduces the risk of accidentally exposing credentials in version control.

## Conclusion

In this post, we've looked at how to set up the official set of Model Context Protocol servers from the [modelcontextprotocol](https://github.com/modelcontextprotocol/servers) organisation:

- server-time
- server-fetch
- server-filesystem
- server-git

The key steps we've covered:

1. Install the `uv` package with `brew install uv` (if you don't already have it)
2. Register the time, fetch, and git servers using `uvx` (with proper timezone for the time server)
3. Register the filesystem server using `npx` with explicit directory permissions
4. Check connections using the `/mcp` command inside Claude Code
5. Sort out connection issues using the `--mcp-debug` flag when needed

These servers greatly expand Claude Code's capabilities by connecting it to external tools and services. With these MCP servers properly configured, Claude becomes a much more powerful coding assistant that can:

- Access accurate time and date information
- Fetch and process web content
- Work with files and directories
- Execute git version control commands

The Model Context Protocol continues to develop, and we'll likely see more servers added over time. By setting up these servers properly, you'll get the most out of Claude Code's extensible design.

For more details on MCP, have a look at the [official documentation](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/tutorials#set-up-model-context-protocol-mcp) and the [MCP servers repository](https://github.com/modelcontextprotocol/servers).
