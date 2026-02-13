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
"""
NetApp RRS SOAR App

This is the main application file that defines the SOAR app and registers all actions.
All models, configurations, and action implementations are organized in separate modules.
"""

from soar_sdk.abstract import SOARClient
from soar_sdk.app import App
from soar_sdk.logging import getLogger

from actions.connectivity import test_connectivity_handler
from models.enrich_ip.EnrichIpOutput import EnrichIpOutput
from models.enrich_ip.EnrichIpParams import EnrichIpParams
from models.enrich_storage.EnrichStorageParams import EnrichStorageParams
from models.enrich_storage.EnrichStorageOutput import EnrichStorageOutput
from models.take_snapshot.TakeSnapshotParams import TakeSnapshotParams
from models.take_snapshot.TakeSnapshotOutput import TakeSnapshotOutput
from models.volume_offline.VolumeOfflineParams import VolumeOfflineParams
from models.volume_offline.VolumeOfflineOutput import VolumeOfflineOutput
from models.job_status.JobStatusParams import JobStatusParams
from models.job_status.JobStatusOutput import JobStatusOutput
from asset import Asset
from config.constants import (
    APP_NAME,
    APP_TYPE,
    LOGO_FILE,
    LOGO_DARK_FILE,
    PRODUCT_VENDOR,
    PRODUCT_NAME,
    PUBLISHER,
    APP_ID,
    FIPS_COMPLIANT,
)

logger = getLogger()

# Initialize the SOAR app with configuration from constants
app = App(
    name=APP_NAME,
    app_type=APP_TYPE,
    logo=LOGO_FILE,
    logo_dark=LOGO_DARK_FILE,
    product_vendor=PRODUCT_VENDOR,
    product_name=PRODUCT_NAME,
    publisher=PUBLISHER,
    appid=APP_ID,
    fips_compliant=FIPS_COMPLIANT,
    asset_cls=Asset,
)


@app.test_connectivity()
def test_connectivity(soar: SOARClient, asset: Asset) -> None:
    logger.info(
        f"test_connectivity: Starting connectivity test domain={asset.rr_saas_domain}"
    )
    test_connectivity_handler(asset)


# Register IP enrich_ip action
app.register_action(
    "actions.enrich_ip:enrich_ip_address_handler",
    name="enrich ip address",
    identifier="enrich_ip_address",
    description="Enrich IP address with additional information",
    action_type="investigate",
    view_handler="view_handlers.enrich_ip_view:render_enrich_ip_jobs_handler",
    view_template="enrich_ip_results.html",
    params_class=EnrichIpParams,
    output_class=EnrichIpOutput,
)

# Register job status action
app.register_action(
    "actions.job_status:job_status_handler",
    name="check job status",
    identifier="check_job_status",
    description="Check the status of an enrichment job",
    action_type="investigate",
    read_only=True,
    params_class=JobStatusParams,
    output_class=JobStatusOutput,
)

# Register enrich storage action
app.register_action(
    "actions.enrich_storage:enrich_storage_handler",
    name="enrich storage",
    identifier="enrich_storage",
    description="Enrich storage information for a given agent and system",
    action_type="investigate",
    read_only=True,
    params_class=EnrichStorageParams,
    output_class=EnrichStorageOutput,
)

app.register_action(
    "actions.take_snapshot:take_snapshot_handler",
    name="take snapshot",
    identifier="take_snapshot",
    description="Take snapshot of a volume",
    action_type="generic",
    read_only=True,
    params_class=TakeSnapshotParams,
    output_class=TakeSnapshotOutput,
)

app.register_action(
    "actions.volume_offline:volume_offline_handler",
    name="volume offline",
    identifier="volume_offline",
    description="Take volume offline",
    action_type="generic",
    read_only=True,
    params_class=VolumeOfflineParams,
    output_class=VolumeOfflineOutput,
)

if __name__ == "__main__":
    app.cli()
