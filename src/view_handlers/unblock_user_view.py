# Copyright (c) 2026 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""View handler for unblock user results."""

from soar_sdk.logging import getLogger

from models.unblock_user.UnblockUserOutput import UnblockUserOutput

logger = getLogger()


def render_unblock_user_handler(output: UnblockUserOutput) -> dict:
    """
    View handler for rendering unblock user results.

    Transforms the UnblockUserOutput model into a dictionary for template rendering.

    Args:
        output: The UnblockUserOutput model containing result message

    Returns:
        dict: Dictionary representation of the output for template rendering
    """
    logger.info("render_unblock_user_handler: Processing unblock user output")
    return output.model_dump()
