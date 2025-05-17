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
"""Tests for the main function."""

from awslabs.hello_world_mcp_server.server import main
from unittest.mock import patch


class TestMain:
    """Tests for the main entry point."""

    @patch('awslabs.hello_world_mcp_server.server.mcp.run')
    @patch('sys.argv', ['awslabs.hello-world-mcp-server'])
    def test_main_default(self, mock_run) -> None:
        """main should run with default transport."""
        main()
        mock_run.assert_called_once()
        assert mock_run.call_args[1].get('transport') is None

    @patch('awslabs.hello_world_mcp_server.server.mcp.run')
    @patch('sys.argv', ['awslabs.hello-world-mcp-server', '--sse', '--port', '9999'])
    def test_main_sse(self, mock_run) -> None:
        """main should run with SSE when flag provided."""
        main()
        mock_run.assert_called_once()
        assert mock_run.call_args[1].get('transport') == 'sse'
        from awslabs.hello_world_mcp_server.server import mcp
        assert mcp.settings.port == 9999
