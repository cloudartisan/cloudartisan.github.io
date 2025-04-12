---
title: "Setting Up Official MCP Servers with Claude Code"
date: 2025-04-11
draft: false
description: "How to install and configure official Model Context Protocol (MCP) servers to extend Claude Code's capabilities"
tags: ["AI", "Claude", "MCP", "CLI"]
---

## What Are MCP Servers?

MCP (Model Context Protocol) servers extend Claude Code's capabilities by allowing it to interact with external tools and services. These servers act as bridges between Claude's AI capabilities and various development tools, providing additional functionality beyond what's built into Claude Code.

For comprehensive information about the Model Context Protocol, visit the [official MCP website](https://modelcontextprotocol.io/) or check out the [MCP servers GitHub repository](https://github.com/modelcontextprotocol/servers).

This post focuses on setting up the official reference MCP servers from the Model Context Protocol organization.

## Why Use MCP Servers?

MCP servers enable Claude to:

- Install packages and dependencies without requiring direct system access
- Connect to specialised development tools
- Execute code in various programming languages
- Access project-specific utilities
- Integrate with custom workflows

## Types of MCP Servers

There are many types of MCP servers available, each providing different capabilities. The [official Model Context Protocol servers](https://github.com/modelcontextprotocol/servers) provide a standard set of capabilities:

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

## Setting Up MCP Servers

Setting up MCP servers with Claude Code is simple and straightforward:

The best way to use MCP servers is through the `npx` command, which runs the packages directly without requiring global installation. This ensures you always use the latest version of each server.

To set up the official MCP servers, follow these steps:

1. First, register each MCP server using the Claude Code CLI:

```bash
# Register server-time (date and time operations)
claude mcp add-json server-time --scope user '{
  "command": "npx",
  "args": [
    "@modelcontextprotocol/server-time@latest"
  ]
}'

# Register server-fetch (URL content fetching)
claude mcp add-json server-fetch --scope user '{
  "command": "npx",
  "args": [
    "@modelcontextprotocol/server-fetch@latest"
  ]
}'

# Register server-filesystem (file operations)
claude mcp add-json server-filesystem --scope user '{
  "command": "npx",
  "args": [
    "@modelcontextprotocol/server-filesystem@latest"
  ]
}'

# Register server-git (git operations)
claude mcp add-json server-git --scope user '{
  "command": "npx",
  "args": [
    "@modelcontextprotocol/server-git@latest"
  ]
}'
```

After registration, you can verify that the servers are properly configured:

```bash
claude mcp list
```

This should show all configured MCP servers:

![Screenshot of available MCP servers](/images/2025/04/screenshot_claude_avail_mcp_servers.png)

As shown in the screenshot, when registration is successful, you'll see all four official MCP servers listed with their package paths. Note how each path shows the `@latest` tag to ensure you're always using the current version.

> **Important Note**: As of April 2025, while the MCP servers can be registered successfully, the actual npm packages may not yet be available in the public npm registry. When starting Claude Code, you might see a message like "4 MCP servers failed to connect" until the packages are officially published. This is expected behavior and doesn't affect the registration process described here.

## MCP Configuration Basics

The `claude mcp` command provides several options for managing MCP servers:

- `add`: Interactive wizard to add a server
- `add-json`: Add a server using JSON configuration
- `list`: View all configured MCP servers
- `remove`: Delete an MCP server
- `get`: View details of a specific server

### Configuration Scopes

When adding MCP servers, you can specify different scopes using the `--scope` flag:

```bash
claude mcp add-json --scope=user server-name '{...configuration...}'
```

Available scopes include:

- `local` (default): Available only in your current session. These servers are temporary and will not persist when you close Claude Code.

- `user`: Available across all your projects on your system. This is recommended for servers you want to use regularly.

- `project`: Available to anyone working on this specific project who has Claude Code installed. These settings are stored in the project's .mcp.json file, making them shareable with your team.

For personal tools that you'll use across multiple projects, the `user` scope is typically the best choice as it reduces duplication and ensures consistent availability.

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
  Command: npx
  Args: @modelcontextprotocol/server-time
```

### Testing Your Installed Servers

You can check which MCP servers are available by asking:

```
What MCP Servers do we have available?
```

Claude will show you all configured MCP servers as demonstrated in the screenshot above.

### Integration Considerations

It's important to note that MCP server integration with Claude Code is an evolving feature. After installation, you may find:

1. **Connection Issues**: You might see notifications about MCP servers failing to connect when starting Claude Code. This often happens when:
   - The registration command uses incorrect package names
   - The specified version is not available
   - There's a network issue preventing npx from fetching the package
   - The package is being fetched for the first time (may take a moment)

2. **Troubleshooting Connection Issues**: If you see a message like "4 MCP servers failed to connect", check:
   - That your registration commands use the correct package names with `@latest`
   - That you're connected to the internet when first running Claude Code
   - That you have executed `npx @modelcontextprotocol/server-time@latest` at least once to pre-fetch the package
   - That no firewalls are blocking JavaScript package downloads

3. **Limited Documentation**: The specific interaction patterns with each server may not be fully documented

4. **Implicit Usage**: Unlike explicit tool calls, MCP servers are designed to be used implicitly through natural language queries

The Model Context Protocol and its server implementations are still maturing, and the integration between the servers and Claude Code is likely to improve over time. For the most up-to-date information on using MCP servers with Claude Code, refer to the [official documentation](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/tutorials#set-up-model-context-protocol-mcp).

## Security Considerations

Always review MCP server configurations before adding them, especially from third-party sources. MCP servers execute commands on your system, so ensure you trust their source and understand what they do.

When using MCP servers that require authentication (like GitHub tokens), follow these security practices:
- Use tokens with the minimum necessary permissions
- Set appropriate expiration dates
- Never share tokens in public forums or commit them to repositories
- Revoke tokens immediately if accidentally exposed

## Conclusion

In this post, we've covered how to install and configure the official set of Model Context Protocol servers from the [modelcontextprotocol](https://github.com/modelcontextprotocol/servers) organization:

- server-time
- server-fetch
- server-filesystem
- server-git

The key steps we've learned:

1. Register the MCP servers with Claude Code using the Claude CLI and npx references
2. Test the connection by running `claude mcp list`
3. Troubleshoot any connection issues that might arise
4. No installation is needed - npx fetches and runs the packages on demand

These servers significantly expand Claude Code's capabilities by providing standardized interfaces to external tools and services. With these official MCP servers properly configured, Claude becomes a more powerful development partner with the ability to:

- Access current time and date information
- Fetch and process web content
- Perform advanced filesystem operations
- Execute git version control commands

The Model Context Protocol is an evolving standard, and more servers are likely to be added over time. By understanding how to properly install and use these servers, you'll be able to take full advantage of Claude Code's extensible architecture.

For more details on MCP, refer to the [official documentation](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/tutorials#set-up-model-context-protocol-mcp) and the [MCP servers repository](https://github.com/modelcontextprotocol/servers).