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
"""Unblock user service for calling RRS unblock user API."""

import httpx
from soar_sdk.logging import getLogger

from asset import Asset
from config.constants import DEFAULT_TIMEOUT, ENDPOINT_UNBLOCK_USER, SSL_VERIFY
from models.unblock_user.UnblockUserOutput import UnblockUserOutput
from models.unblock_user.UnblockUserParams import UnblockUserParams
from utils.url_builder import build_rr_saas_url

logger = getLogger()


def unblock_user_api(
    params: UnblockUserParams, asset: Asset, token: str
) -> UnblockUserOutput:
    """
    Call the unblock user API to unblock a user.

    Args:
        params: Unblock user parameters containing user_id and user_ips
        asset: Asset configuration containing domain
        token: OAuth Bearer token for authentication

    Returns:
        UnblockUserOutput with status message

    Raises:
        Exception: If the API call fails

    Example:
        >>> token = get_oauth_token(asset)
        >>> params = UnblockUserParams(user_id="user123")
        >>> response = unblock_user_api(params, asset, token)
        >>> print(response.message)
    """
    logger.info(f"unblock_user_api: Unblocking user: {params}")

    # Convert Pydantic model to dict, excluding None values
    request_payload = params.model_dump(exclude_none=True)

    # Convert comma-separated user_ips string to list for API
    if request_payload.get("user_ips"):
        request_payload["user_ips"] = [
            ip.strip() for ip in request_payload["user_ips"].split(",")
        ]

    # Build full URL
    url = f"{build_rr_saas_url(asset)}{ENDPOINT_UNBLOCK_USER}"

    # Prepare headers
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    logger.debug(f"unblock_user_api: URL: {url}")
    logger.debug(f"unblock_user_api: Payload: {request_payload}")

    try:
        # Make API call (verify=False to allow self-signed certificates)
        with httpx.Client(timeout=DEFAULT_TIMEOUT, verify=SSL_VERIFY) as client:
            response = client.post(url, json=request_payload, headers=headers)

            # Check if request was successful
            response.raise_for_status()

            logger.info(
                f"unblock_user_api: API call successful. Status: {response.status_code}"
            )

            # Create UnblockUserOutput - API returns empty response
            output = UnblockUserOutput(message="User unblocked successfully")

            logger.info(
                f"unblock_user_api: User unblock completed for {params.user_id or params.user_ips}"
            )

            return output

    except httpx.HTTPStatusError as e:
        error_msg = f"HTTP error occurred: {e.response.status_code} - {e.response.text}"
        logger.error(f"unblock_user_api: {error_msg}")
        raise Exception(error_msg) from e

    except httpx.RequestError as e:
        error_msg = f"Request error occurred: {e!s}"
        logger.error(f"unblock_user_api: {error_msg}")
        raise Exception(error_msg) from e

    except Exception as e:
        error_msg = f"Unexpected error: {e!s}"
        logger.error(f"unblock_user_api: {error_msg}")
        raise Exception(error_msg) from e
