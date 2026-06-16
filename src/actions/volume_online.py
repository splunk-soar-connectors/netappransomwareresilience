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
from soar_sdk.abstract import SOARClient
from soar_sdk.logging import getLogger
from soar_sdk.exceptions import ActionFailure
from asset import Asset
from models.volume_online.VolumeOnlineParams import VolumeOnlineParams
from models.volume_online.VolumeOnlineOutput import VolumeOnlineOutput
from services.auth_service_api import get_oauth_token_api
from services.volume_online_api import volume_online_api

logger = getLogger()


def volume_online_handler(
    params: VolumeOnlineParams, soar: SOARClient[VolumeOnlineOutput], asset: Asset
) -> VolumeOnlineOutput:
    """
    Take volume online by calling the REST API.

    This action posts volume data to the API and returns the created job details.

    Args:
        params: VolumeOnline parameters containing volume ID and working environment details
        soar: SOAR client for setting summary and messages
        asset: Asset configuration

    Returns:
        VolumeOnlineOutput with the created job details including ID and status
    """
    logger.info(
        f"volume_online_handler: Starting volume online process: {params=}, Account: {asset.account_id}"
    )

    try:
        # Get OAuth token
        token = get_oauth_token_api(asset)
        logger.debug("volume_online_handler: OAuth token retrieved successfully")

        # Call the volume online service
        response_data = volume_online_api(params, asset, token)

        soar.set_summary(response_data)
        soar.set_message(f"Volume '{params.volume_id}' taken online successfully")

        logger.info(
            f"volume_online_handler: Volume online process completed for volume {params.volume_id}"
        )

        return response_data

    except Exception as e:
        error_msg = f"Failed to take volume online: {e!s}"
        logger.error(f"volume_online_handler: {error_msg}")
        raise ActionFailure(error_msg) from e
