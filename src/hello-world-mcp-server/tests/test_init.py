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
"""Tests for package initialization."""

import importlib
import re


class TestInit:
    """Validate __init__ contents."""

    def test_version(self) -> None:
        """__version__ should follow semantic versioning."""
        import awslabs.hello_world_mcp_server as pkg
        assert hasattr(pkg, '__version__')
        assert isinstance(pkg.__version__, str)
        assert re.match(r'^\d+\.\d+\.\d+$', pkg.__version__)

    def test_module_reload(self) -> None:
        """Module should reload without errors."""
        import awslabs.hello_world_mcp_server as pkg
        original = pkg.__version__
        importlib.reload(pkg)
        assert pkg.__version__ == original
