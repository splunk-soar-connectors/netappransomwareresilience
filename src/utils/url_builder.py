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
"""URL builder utility for constructing RR SaaS endpoints."""

from asset import Asset
from config.constants import RR_SAAS_API_PATH


def build_rr_saas_url(asset: Asset) -> str:
    """
    Construct the RR SaaS API URL using the provided domain.

    Args:
        asset: The Asset object containing the RR SaaS domain name (e.g., "snapcenter.cloudmanager.cloud.netapp.com")

    Returns:
        Complete URL string in format: https://{domain}/rps/v1/account/

    Example:
        >>> build_rr_saas_url("snapcenter.cloudmanager.cloud.netapp.com")
        'https://snapcenter.cloudmanager.cloud.netapp.com/rps/v1/account/'
    """
    # Remove any leading/trailing whitespace
    domain = asset.rr_saas_domain.strip()

    # Remove protocol if already present
    if domain.startswith("https://"):
        domain = domain[8:]
    elif domain.startswith("http://"):
        domain = domain[7:]

    # Remove trailing slash if present
    domain = domain.rstrip("/")

    # Construct the URL
    url = f"https://{domain}{RR_SAAS_API_PATH}/{asset.account_id}"

    return url
