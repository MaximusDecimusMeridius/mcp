# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance
# with the License. A copy of the License is located at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# or in the 'license' file accompanying this file. This file is distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES
# OR CONDITIONS OF ANY KIND, express or implied. See the License for the specific language governing permissions
# and limitations under the License.
"""awslabs Hello World MCP Server implementation."""

import argparse
import os
import sys
from loguru import logger
from mcp.server.fastmcp import FastMCP

logger.remove()
logger.add(sys.stderr, level=os.getenv('FASTMCP_LOG_LEVEL', 'INFO'))

mcp = FastMCP(
    'awslabs.hello-world-mcp-server',
    instructions="""Simple MCP server that greets the user.""",
    dependencies=['loguru'],
)


@mcp.tool()
async def hello_world() -> str:
    """Return a friendly greeting."""
    return 'Hello, world!'


def main() -> None:
    """Run the MCP server."""
    parser = argparse.ArgumentParser(description='Hello World MCP server')
    parser.add_argument('--sse', action='store_true', help='Use SSE transport')
    parser.add_argument('--port', type=int, default=8888, help='Port to run the server on')
    args = parser.parse_args()

    if args.sse:
        mcp.settings.port = args.port
        mcp.run(transport='sse')
    else:
        mcp.run()


if __name__ == '__main__':  # pragma: no cover
    main()
