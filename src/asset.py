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
"""Asset model definition for NetApp RPS SOAR app."""

from soar_sdk.asset import BaseAsset, AssetField


class Asset(BaseAsset):
    """
    Asset configuration for NetApp RPS connector.

    Attributes:
        base_url: Base URL for the API endpoint
        api_key: API key for authentication
        key_header: Header name to use for API key
        api_token: API token value
        timezone: Timezone without default
        timezone_with_default: Timezone with default value
    """

    rr_saas_domain: str = AssetField(
        default="snapcenter.cloudmanager.cloud.netapp.com",
        description="RR SaaS domain name",
    )
    client_id: str = AssetField(
        sensitive=True, description="Client ID for authentication"
    )
    client_secret: str = AssetField(
        sensitive=True, description="Client Secret for authentication"
    )
    account_id: str = AssetField(
        sensitive=False, description="Account ID for the RR SaaS account"
    )
