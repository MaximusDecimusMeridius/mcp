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
"""Tests for the hello world MCP server."""

import asyncio
from awslabs.hello_world_mcp_server.server import hello_world, mcp


class TestHelloWorld:
    """Tests for the hello_world tool."""

    def test_hello_world(self) -> None:
        """hello_world should return a greeting."""
        result = asyncio.run(hello_world())
        assert result == 'Hello, world!'


class TestMCP:
    """Tests for FastMCP initialization."""

    def test_mcp_name(self) -> None:
        """Ensure MCP is initialized with the correct name."""
        assert mcp.name == 'awslabs.hello-world-mcp-server'
