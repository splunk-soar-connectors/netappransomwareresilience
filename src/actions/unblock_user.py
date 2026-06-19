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
"""Unblock user action for NetApp RRS SOAR app."""

from soar_sdk.abstract import SOARClient
from soar_sdk.exceptions import ActionFailure
from soar_sdk.logging import getLogger

from asset import Asset
from models.unblock_user.UnblockUserOutput import UnblockUserOutput
from models.unblock_user.UnblockUserParams import UnblockUserParams
from services.auth_service_api import get_oauth_token_api
from services.unblock_user_api import unblock_user_api

logger = getLogger()


def unblock_user_handler(
    params: UnblockUserParams, soar: SOARClient[UnblockUserOutput], asset: Asset
) -> UnblockUserOutput:
    """
    Unblock a previously blocked user from accessing storage resources.

    This action unblocks a user based on user_id and/or client IPs.

    Args:
        params: Unblock user parameters including user_id and user_ips
        soar: SOAR client for setting summary and messages
        asset: Asset configuration

    Returns:
        Unblock user output with status message
    """
    logger.debug(
        f"unblock_user_handler: User ID: {params.user_id}, IPs: {params.user_ips}"
    )

    try:
        # Get OAuth token
        token = get_oauth_token_api(asset)
        logger.debug("unblock_user_handler: OAuth token retrieved successfully")

        # Call the unblock user service
        logger.info("unblock_user_handler: calling unblock_user_api")
        output = unblock_user_api(params, asset, token)

        soar.set_summary(output)
        soar.set_message(
            f"User '{params.user_id or params.user_ips}' unblocked successfully"
        )

        logger.info(
            f"unblock_user_handler: Unblock user completed for {params.user_id or params.user_ips}"
        )

        return output

    except Exception as e:
        error_msg = f"Failed to unblock user: {e!s}"
        logger.error(f"unblock_user_handler: {error_msg}")
        raise ActionFailure(error_msg) from e
