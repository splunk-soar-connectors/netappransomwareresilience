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
Configuration and constants for NetApp RPS SOAR app.
"""

# App Metadata
APP_NAME = "NetApp Ransomware Resilience"
APP_TYPE = "generic"
PRODUCT_VENDOR = "NetApp"
PRODUCT_NAME = "NetApp Ransomware Resilience"
PUBLISHER = "NetApp"
APP_ID = "8612e34c-5341-49d3-8a57-81465ca4f06c"
FIPS_COMPLIANT = False

# Logos
LOGO_FILE = "logo.svg"
LOGO_DARK_FILE = "logo_dark.svg"

# OAuth Configuration
OAUTH_CONFIG = {
    "ENDPOINT": "https://staging-netapp-cloud-account.auth0.com/oauth/token",
    "GRANT_TYPE": "client_credentials",
    "AUDIENCE": "https://api.cloud.netapp.com",
    "METHOD": "POST",
    "CONTENT_TYPE": "application/x-www-form-urlencoded",
}

# API Configuration
RR_SAAS_API_PATH = "/bavinash/v1/account"
# API Endpoints
ENDPOINT_TEST_CONNECTION = "/test-connection"
ENDPOINT_ENRICH_IP = "/enrich/ip-address"
ENDPOINT_ENRICH_STORAGE = "/enrich/storage"
ENDPOINT_VOLUME_OFFLINE = "/storage/take-volume-offline"
ENDPOINT_TAKE_SNAPSHOT = "/storage/take-snapshot"
ENDPOINT_JOB_STATUS = "/job/status"

# API Headers
AUTHORIZATION_HEADER = "Authorization"


# HTTP Methods
HTTP_METHOD_GET = "GET"
HTTP_METHOD_POST = "POST"
HTTP_METHOD_PUT = "PUT"
HTTP_METHOD_DELETE = "DELETE"
HTTP_METHOD_PATCH = "PATCH"

# Response codes
HTTP_OK = 200
HTTP_CREATED = 201
HTTP_BAD_REQUEST = 400
HTTP_UNAUTHORIZED = 401
HTTP_FORBIDDEN = 403
HTTP_NOT_FOUND = 404
HTTP_SERVER_ERROR = 500

# Timeout settings (in seconds)
DEFAULT_TIMEOUT = 30
CONNECTION_TIMEOUT = 10

# SSL/TLS Configuration
SSL_VERIFY = False  # Set to False to allow self-signed certificates (dev/staging only)
