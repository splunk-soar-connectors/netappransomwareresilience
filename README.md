# NetApp Ransomware Resilience (RRS) - Splunk SOAR App

![Python Version](https://img.shields.io/badge/python-3.13%2B-blue)
![Splunk SOAR SDK](https://img.shields.io/badge/splunk--soar--sdk-%3E%3D3.8.2-orange)
![httpx](https://img.shields.io/badge/httpx-%3E%3D0.27.0-green)
![Pydantic](https://img.shields.io/badge/pydantic-v2-red)

A comprehensive Splunk SOAR integration for NetApp Ransomware Resilience Service (RRS), enabling automated threat response and data protection actions through SOAR playbooks.

## 📋 Table of Contents

- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Testing Actions](#testing-actions)
- [Available Actions](#available-actions)
- [Building the App](#building-the-app)

## 🔧 Prerequisites

- Python 3.13 or higher (< 3.15)
- Splunk SOAR SDK >= 3.8.2
- httpx >= 0.27.0
- NetApp RRS account with API credentials

## 📦 Setup

For first-time setup and installation of the Splunk SOAR SDK, refer to the official documentation:

👉 **[Splunk SOAR SDK Installation Guide](https://phantomcyber.github.io/splunk-soar-sdk/getting_started/installation.html)**

Once the SDK is installed, clone the repository and set up the environment:

```bash
git clone <repository-url>
cd rrs-splunk-soar-app

# Install dependencies (creates venv and installs packages)
uv sync

# Activate the virtual environment (optional - for running shell commands)
source .venv/bin/activate
```

## 📁 Project Structure

```
rrs-splunk-soar-app/
├── src/
│   ├── app.py                      # Main SOAR application entry point
│   ├── asset.py                    # Asset configuration model
│   │
│   ├── actions/                    # Action handlers (orchestration layer)
│   │   ├── __init__.py
│   │   ├── connectivity.py         # Test connectivity action
│   │   ├── enrich_ip.py           # IP enrichment action
│   │   ├── enrich_storage.py      # Storage enrichment action
│   │   ├── job_status.py          # Job status checking action
│   │   ├── take_snapshot.py        # Snapshot creation action
│   │   └── volume_offline.py       # Volume offline action
│   │
│   ├── services/                   # Business logic and API calls
│   │   ├── __init__.py
│   │   ├── auth_service_api.py     # OAuth token management (get_oauth_token_api)
│   │   ├── enrich_ip_api.py        # IP enrichment API service (enrich_ip_api)
│   │   ├── enrich_storage_api.py   # Storage enrichment API service (enrich_storage_api)
│   │   ├── job_status_api.py       # Job status polling service (get_job_status_api)
│   │   ├── take_snapshot_api.py    # Snapshot API service (take_snapshot_api)
│   │   └── volume_offline_api.py   # Volume offline API service (volume_offline_api)
│   │
│   ├── models/                     # Pydantic models for type safety
│   │   ├── __init__.py
│   │   ├── asset.py                # Asset model
│   │   ├── enrich_ip/              # IP enrichment models
│   │   ├── enrich_storage/         # Storage enrichment models
│   │   ├── job_status/             # Job status models
│   │   ├── take_snapshot/          # Snapshot models
│   │   └── volume_offline/         # Volume offline models
│   │
│   ├── config/                     # Configuration and constants
│   │   ├── __init__.py
│   │   └── constants.py            # API endpoints and app metadata
│   │
│   ├── utils/                      # Utility functions
│   │   ├── __init__.py
│   │   └── url_builder.py          # URL construction helpers
│   │
│   └── test_params/                # Test parameter files
│       ├── test_asset.json         # Asset configuration for testing (gitignored)
│       ├── enrich_ip.json          # IP enrichment test parameters
│       ├── enrich_storage.json     # Storage enrichment test parameters
│       ├── job_status.json         # Job status test parameters
│       ├── take_snapshot.json      # Snapshot test parameters
│       └── volume_offline.json     # Volume offline test parameters
│
├── pyproject.toml                  # Project configuration and dependencies
├── README.md                       # This file
└── release_notes/
    └── unreleased.md               # Release notes
```

## 🔑 Configuration

### Asset Configuration

Create an asset configuration file (`test_asset.json`) with your NetApp RRS credentials:

```json
{
  "rr_saas_domain": "snapcenter.cloudmanager.cloud.netapp.com",
  "client_id": "your-client-id-here",
  "client_secret": "your-client-secret-here",
  "account_id": "your-account-id-here"
}
```

**Asset Fields:**

- **`rr_saas_domain`**: RR SaaS domain name (default: `snapcenter.cloudmanager.cloud.netapp.com`)
- **`client_id`**: OAuth2 Client ID for authentication (sensitive field, encrypted in SOAR)
- **`client_secret`**: OAuth2 Client Secret for authentication (sensitive field, encrypted in SOAR)
- **`account_id`**: NetApp account ID for the RR SaaS account

**Note**: `test_asset.json` is gitignored to protect sensitive credentials.

## 🧪 Testing Actions

Run actions locally using the following commands:

### Test Connectivity

Verify authentication and connectivity to NetApp RRS API:

```bash
python src/app.py action test-connectivity -a ./src/test_params/test_asset.json
```

### Enrich IP Address

Enrich an IP address with threat intelligence:

```bash
python src/app.py action enrich_ip_address -p ./src/test_params/enrich_ip.json -a ./src/test_params/test_asset.json
```

**Parameters** (`enrich_ip.json`):

```json
{
  "ip_address": "192.168.1.100"
}
```

### Enrich Storage

Get storage volume information for an agent and system:

```bash
python src/app.py action enrich_storage -p ./src/test_params/enrich_storage.json -a ./src/test_params/test_asset.json
```

**Parameters** (`enrich_storage.json`):

```json
{
  "agent_id": "your-agent-id",
  "system_id": "your-system-id"
}
```

### Check Job Status

Check the status of an asynchronous job:

```bash
python src/app.py action check_job_status -p ./src/test_params/job_status.json -a ./src/test_params/test_asset.json
```

**Parameters** (`job_status.json`):

```json
{
  "job_id": "job-123456"
}
```

### Take Snapshot

Create a snapshot of a volume:

```bash
python src/app.py action take_snapshot -p ./src/test_params/take_snapshot.json -a ./src/test_params/test_asset.json
```

**Parameters** (`take_snapshot.json`):

```json
{
  "agent_id": "agent-123",
  "system_id": "sys-456",
  "volume_uuid": "vol-uuid-789",
  "snapshot_name": "snapshot-backup-001"
}
```

### Take Volume Offline

Take a volume offline for incident response:

```bash
python src/app.py action volume_offline -p ./src/test_params/volume_offline.json -a ./src/test_params/test_asset.json
```

**Parameters** (`volume_offline.json`):

```json
{
  "agent_id": "agent-123",
  "system_id": "sys-456",
  "volume_uuid": "vol-uuid-789"
}
```

## 🎯 Available Actions

| Action | Identifier | Type | Description |
|--------|-----------|------|-------------|
| Test Connectivity | `test_connectivity` | Test | Verify API credentials and connectivity |
| Enrich IP Address | `enrich_ip_address` | Investigate | Enrich IP with threat intelligence |
| Enrich Storage | `enrich_storage` | Investigate | Get volume information for agent/system |
| Check Job Status | `check_job_status` | Investigate | Check status of asynchronous jobs |
| Take Snapshot | `take_snapshot` | Generic | Create volume snapshot |
| Volume Offline | `volume_offline` | Generic | Take volume offline |

## 🏗️ Architecture

This app follows a clean architecture pattern with separation of concerns:

- **Actions** (`src/actions/`): Orchestration layer that handles SOAR-specific logic
- **Services** (`src/services/`): Business logic and API communication (all functions use `_api` suffix)
- **Models** (`src/models/`): Pydantic v2 models for type safety and validation
- **Config** (`src/config/`): Centralized configuration and constants

### Service Functions Convention

All service functions follow the naming pattern `*_api`:

- `get_oauth_token_api()` - OAuth authentication
- `enrich_ip_api()` - IP enrichment
- `enrich_storage_api()` - Storage enrichment
- `get_job_status_api()` - Job status polling
- `take_snapshot_api()` - Snapshot creation
- `volume_offline_api()` - Volume offline

## 📌 Important Files

- **`src/app.py`**: Main entry point, registers all actions using `app.register_action()`
- **`src/asset.py`**: Asset configuration model with sensitive field handling
- **`src/config/constants.py`**: All API endpoints, OAuth config, and app metadata
- **`src/services/auth_service_api.py`**: Authentication service for OAuth token management
- **`pyproject.toml`**: Project dependencies and SOAR app configuration

## 🔐 Security Features

- SSL/TLS certificate verification (configurable via `SSL_VERIFY` in constants)
- Sensitive fields (client_id, client_secret) are encrypted when stored in SOAR
- OAuth 2.0 authentication with Bearer tokens for all API calls
- Test asset files are gitignored to prevent credential leaks

## 🛠️ Development

### Adding a New Action

Follow this template when adding new actions:

1. **Models**: Create `[ActionName]Params.py` and `[ActionName]Output.py` in `src/models/[action_name]/`
1. **Service**: Create `[action_name]_api.py` in `src/services/` (follow `enrich_ip_api.py` pattern)
1. **Action**: Create `[action_name].py` in `src/actions/` (follow `enrich_ip.py` pattern)
1. **Constants**: Add endpoint constant to `src/config/constants.py`
1. **Registration**: Import and register in `src/app.py`
1. **Test Params**: Create `[action_name].json` in `src/test_params/`

All service functions must use the `_api` suffix (e.g., `my_action_api()`).

### Code Conventions

- Use Pydantic v2 for all models with `ConfigDict(populate_by_name=True)`
- Use `Field(default_factory=list)` for mutable defaults (not `= []`)
- Service functions return typed models, not raw dicts
- Actions handle SOAR-specific logic (summary, messages, error conversion)
- Services handle API communication and business logic

## 🔨 Building the App

Build the SOAR app package for deployment:

```bash
soarapps package build
```

This creates a `.tgz` file in the current directory that can be installed on Splunk SOAR.

### Package Installation

1. Log in to your Splunk SOAR instance
1. Navigate to **Apps** → **Install App**
1. Upload the generated `.tgz` file
1. Configure the asset with your NetApp RRS credentials

## 🧪 Testing

All actions can be tested locally before deployment:

```bash
# Run all tests with different parameter files
python src/app.py action <action_identifier> -p ./src/test_params/<params_file>.json -a ./src/test_params/test_asset.json
```

Ensure your `test_asset.json` has valid credentials before testing.

## 📚 API Endpoints

The app integrates with the following NetApp RRS API endpoints:

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/enrich/ip-address` | POST | IP address enrichment |
| `/enrich/storage` | GET | Storage volume information |
| `/storage/take-snapshot` | POST | Create volume snapshot |
| `/storage/take-volume-offline` | POST | Take volume offline |
| `/job/status` | GET | Check job status |

All endpoints are defined in `src/config/constants.py`.

## 🐛 Troubleshooting

### SSL Certificate Errors

If you encounter SSL certificate errors with self-signed certificates:

- Set `SSL_VERIFY = False` in `src/config/constants.py` (for dev/staging only)
- For production, use proper SSL certificates and set `SSL_VERIFY = True`

### Import Errors

- Ensure virtual environment is activated: `source .venv/bin/activate`
- Reinstall dependencies: `uv sync`

### Authentication Failures

- Verify client_id and client_secret in `test_asset.json`
- Check OAuth endpoint configuration in `constants.py`
- Ensure domain is correct (e.g., `your-domain.cloud.netapp.com`)

## 📝 Notes

- Sensitive fields (client_id, client_secret) are encrypted when stored in SOAR
- All API calls use secure OAuth 2.0 authentication with Bearer tokens
- Service layer returns typed Pydantic models for better IDE support and type safety
- All service functions follow the `*_api` naming convention for consistency

## 🔗 Resources

- [Splunk SOAR SDK Documentation](https://phantomcyber.github.io/splunk-soar-sdk/)
- [Splunk SOAR SDK GitHub](https://github.com/phantomcyber/splunk-soar-sdk)

______________________________________________________________________

**Version**: 1.0.0\
**Maintained by**: NetApp RRS Team
