# Hello World MCP Server

A minimal MCP server that exposes a single `hello_world` tool returning a friendly greeting.

## Prerequisites
- Python 3.10 or newer
- [uv](https://github.com/astral-sh/uv) package manager

## Installation
Example configuration using `uvx`:
```json
{
  "mcpServers": {
    "awslabs.hello-world-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.hello-world-mcp-server@latest"],
      "env": {"FASTMCP_LOG_LEVEL": "ERROR"},
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

## Tools
- `hello_world` &ndash; returns `"Hello, world!"`
