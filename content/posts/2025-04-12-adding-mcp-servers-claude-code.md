---
title: "Setting Up MCP Servers with Claude Code"
date: 2025-04-12
draft: false
description: "How to install and configure Model Context Protocol (MCP) servers to extend Claude Code's capabilities"
tags: ["AI", "Claude", "MCP", "CLI"]
---

## What Are MCP Servers?

MCP (Model Context Protocol) servers extend AI Assistants' capabilities by connecting them to external tools and services.

Recently, Claude Code gained support for MCP servers, enabling integration with more specialised services like Stripe, Cloudflare, Supabase, Blender, and a whole lot more.

This post demonstrates setting up some simple reference MCP servers. These servers won't dramatically enhance Claude Code, since it already has built-in tools for filesystem, git, and web fetching. However, they serve as a gentle introduction to installing and configuring MCP servers without having to worry about overly-complex configuration. We can tackle more advanced integrations later in a future post.

For more details about the Model Context Protocol, have a look at the [official MCP website](https://modelcontextprotocol.io/) or the [MCP servers GitHub repository](https://github.com/modelcontextprotocol/servers). 

## Why Use MCP Servers?

MCP servers enable Claude Code to:

- Use specialised development tools
- Access a wide range of APIs and SaaS
- Integrate with custom workflows
- Make use of reusable prompt templates

## Types of MCP Servers

There are many types of MCP servers available, each providing different capabilities. You can explore available MCP servers at community directories like [mcp.so](https://mcp.so) and [smithery.ai](https://smithery.ai).

The [reference Model Context Protocol servers](https://github.com/modelcontextprotocol/servers?tab=readme-ov-file#-reference-servers) provide a standard set of capabilities, including:

- `server-fetch`: For fetching content from URLs and web resources
- `server-time`: For accurate date and time operations
- `server-filesystem`: For working with files and directories
- `server-git`: For advanced Git operations and version control
- `server-github`: For direct GitHub integration (repositories, issues, PRs)
- `server-memory`: For persistent knowledge storage across sessions
- and more...

We are going to set up a few of these servers as a learning exercise. That said, Claude Code already has native capabilities for filesystem access, git operations, and basic web fetching. The real power of MCP comes when you integrate more specialised servers, which typically require API keys and more complex configuration so we'll cover those in a future post.

## Setting Up MCP Servers

Setting up MCP servers with Claude Code is fairly simple:

The best way to use MCP servers depends on the specific server type and your use-case. For local development, an "stdio" server will do fine. And, if you don't want to mess with having many Docker containers running, most people will do fine with running them through `uvx` (for Python) or `npx` (for Node.js). For the purposes of this post we'll be sticking with local and simple.

To set up the reference MCP servers to run via `uvx` and `npx`, follow these steps...

First, register each MCP server using the Claude Code CLI:

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

As shown in the screenshot, when registration is successful, you'll see all four reference MCP servers listed.

> *Note:* We use `uvx` for the time, fetch, and git servers, and `npx` for the filesystem server simply because they're written in different languages (Python and Node.js).

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
- `user`: Available across all your projects on your system. This is stored in `~/.claude.json` and is my recommended choice for tools you'll use regularly.
- `project`: Available to anyone working on this specific project who has Claude Code installed. These settings are stored in the project's `.mcp.json` file, making them shareable with your team.

For personal tooling that you intend to reuse, the `user` scope is typically best as it reduces duplication and ensures consistent availability.

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

1. **List Registered Servers**:
   ```bash
   claude mcp list
   ```
   This shows registered servers but doesn't confirm they connect successfully.

2. **Check Connection Status**:
   ```bash
   claude --mcp-debug
   ```
   This launches Claude with detailed MCP connection debugging information.

   Then enter the command:
   ```
   /mcp
   ```
   This displays the connection status of each MCP server, showing either "connected" or "failed" for each one.

   When you run the `/mcp` command inside Claude Code, you should see a status display like this:
   
   ```
   /mcp
     ⎿  MCP Server Status
     ⎿
     ⎿  • server-fetch: connected
     ⎿  • server-filesystem: connected
     ⎿  • server-git: connected
     ⎿  • server-time: connected
   ```

   If any server shows "failed", double check that the server is installed and then verify it's registered correctly.

3. **Test with Natural Language**:
   Once launched, you can test specific MCP servers with natural language queries:
   
   * **Testing server-time**:
     ```
     What time is it now?
     What time is it in San Francisco?
     ```
     
     ![Screenshot of server-time MCP server in action](/images/2025/04/screenshot_claude_time.png)
     
   * **Testing server-git**:
     ```
     What are the recent commits in this repository?
     ```
     
     ![Screenshot of server-git MCP server showing recent commits](/images/2025/04/screenshot_claude_recent_commits.png)
     
   * **Testing server-fetch**:
     ```
     What's the latest news on Anthropic's website?
     ```
     
     ![Screenshot of server-fetch MCP server fetching Anthropic news](/images/2025/04/screenshot_claude_get_news.png)
     
### Integration Considerations

MCP server integration with Claude Code is still developing. Some challenges I found included:

1. **Connection Issues**: Servers may fail to connect due to incorrect configuration or, for example, mixing up `npx` and `uvx` (like I did multiple times!).

2. **Limited Documentation**: Usage patterns with each server may not be fully documented.

3. **Implicit Usage**: MCP servers are designed for natural language queries rather than explicit tool calls and sometimes I had trouble crafting the query I needed to use the tool I wanted.

The Model Context Protocol and its server implementations are still maturing. Integration between the servers and Claude Code is likely to improve over time. For the most up-to-date information on using MCP servers with Claude Code, refer to the [official documentation](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/tutorials#set-up-model-context-protocol-mcp).

## Beyond Reference Servers: The MCP Ecosystem

The reference servers are just the beginning. As mentioned earlier, the real power will come from specialised servers that offer capabilities beyond Claude Code's native features. Some examples:

   - [Cloudflare](https://mcp.so/server/cloudflare): Manage Cloudflare DNS, Workers, and more
   - [Brave Search](https://mcp.so/server/brave-search/modelcontextprotocol): Privacy-focused web search integration
   - [Firecrawl](https://mcp.so/server/firecrawl-mcp-server/mendableai): Specialised document search and retrieval
   - [BrowserBase](https://mcp.so/server/mcp-server-browserbase/browserbase): Browser automation and web interaction
   - [Airbnb](https://github.com/openbnb-org/mcp-server-airbnb): Airbnb search and listing details
   - [Obsidian](https://github.com/MarkusPfundstein/mcp-obsidian): Integration with Obsidian knowledge base
   - [Playwright](https://github.com/microsoft/playwright-mcp): Automation testing with Playwright
   - and many many more

There are several ways to discover MCP servers:

1. **Community Directories**:
   - [mcp.so](https://mcp.so): A growing directory of available MCP servers
   - [smithery.ai](https://smithery.ai): Package manager and discovery for MCP

2. **Package Registries**:
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

When choosing alternative servers, pay special attention to security considerations and the reputation of the package maintainers. It's a wild world out there. Just think of all the API keys you might be configuring in one place and all the MCP server code you might _not_ be reviewing...

## Security Considerations

### Trust and Permissions

Always review MCP server configurations before adding them. MCP servers execute commands on your system, context can be shared amongst them, so ensure you trust their source and understand what they're doing.

When using MCP servers that require authentication (like GitHub tokens), follow these security practices:
- Use tokens with the minimum necessary permissions
- Set appropriate expiration dates
- Never share tokens in public forums or commit them to repositories
- Revoke tokens immediately if accidentally exposed


## Conclusion

With MCP servers, Claude Code seamlessly combines capabilities without explicit tool requests, maintaining natural conversations while accessing specialised functionality.

The reference servers we've set up provide an introduction to the MCP ecosystem, though they overlap with Claude Code's built-in features. The real potential comes from specialised servers with unique capabilities.

In this post, we've:

1. Set up four reference MCP servers (time, fetch, filesystem, and git)
2. Learned how to troubleshoot server connections
3. Demonstrated basic server interactions to confirm functionality
4. Explored the broader MCP ecosystem and where to find more specialised servers

These skills establish a foundation we can use for more advanced integrations with Cloudflare, Stripe, Supabase, or other specialised services requiring API keys and complex configuration.

For more on exploring the growing MCP ecosystem, check out [mcp.so](https://mcp.so) and [smithery.ai](https://smithery.ai). For detailed documentation, see the [official Claude Code MCP documentation](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/tutorials#set-up-model-context-protocol-mcp) and the [MCP servers repository](https://github.com/modelcontextprotocol/servers).
