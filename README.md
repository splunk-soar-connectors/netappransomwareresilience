# NetApp Ransomware Resilience

Publisher: NetApp <br>
Connector Version: 1.1.0 <br>
Product Vendor: NetApp <br>
Product Name: NetApp Ransomware Resilience <br>
Minimum Product Version: 7.0.0

A comprehensive Splunk SOAR integration for NetApp Ransomware Resilience Service, enabling automated threat response and data protection actions through SOAR playbooks.

### Configuration variables

This table lists the configuration variables required to operate NetApp Ransomware Resilience. These variables are specified when configuring a NetApp Ransomware Resilience asset in Splunk SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**client_id** | required | password | Client ID for authentication |
**client_secret** | required | password | Client Secret for authentication |
**account_id** | required | string | NetApp Console Account ID |

### Supported Actions

[test connectivity](#action-test-connectivity) - test connectivity <br>
[enrich ip address](#action-enrich-ip-address) - Enrich IP address with additional information <br>
[enrich storage](#action-enrich-storage) - Enrich storage information for a given agent and system <br>
[take snapshot](#action-take-snapshot) - Take snapshot of a volume <br>
[volume offline](#action-volume-offline) - Take volume offline <br>
[volume online](#action-volume-online) - Take volume online <br>
[check job status](#action-check-job-status) - Check the status of an enrichment job <br>
[block user](#action-block-user) - Block user from accessing resources protected by Ransomware Resilience

## action: 'test connectivity'

test connectivity

Type: **test** <br>
Read only: **True**

Basic test for app.

#### Action Parameters

No parameters are required for this action

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string | | success failure |
action_result.message | string | | |
summary.total_objects | numeric | | 1 |
summary.total_objects_successful | numeric | | 1 |

## action: 'enrich ip address'

Enrich IP address with additional information

Type: **investigate** <br>
Read only: **True**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**ip_address** | required | Ip Address | string | |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string | | success failure |
action_result.message | string | | |
action_result.parameter.ip_address | string | | |
action_result.data.\*.jobs.\*.job_id | string | | |
action_result.data.\*.jobs.\*.status | string | | |
action_result.data.\*.jobs.\*.source | string | | |
action_result.data.\*.jobs.\*.agent_id | string | | |
summary.total_objects | numeric | | 1 |
summary.total_objects_successful | numeric | | 1 |

## action: 'enrich storage'

Enrich storage information for a given agent and system

Type: **investigate** <br>
Read only: **True**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**agent_id** | required | Agent Id | string | |
**system_id** | required | System Id | string | |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string | | success failure |
action_result.message | string | | |
action_result.parameter.agent_id | string | | |
action_result.parameter.system_id | string | | |
action_result.data.\*.volumes.\*.volume_uuid | string | | |
action_result.data.\*.volumes.\*.volume_name | string | | |
action_result.data.\*.volumes.\*.svm_name | string | | |
summary.total_objects | numeric | | 1 |
summary.total_objects_successful | numeric | | 1 |

## action: 'take snapshot'

Take snapshot of a volume

Type: **generic** <br>
Read only: **True**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**volume_id** | required | Volume Id | string | |
**agent_id** | required | Agent Id | string | |
**system_id** | required | System Id | string | |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string | | success failure |
action_result.message | string | | |
action_result.parameter.volume_id | string | | |
action_result.parameter.agent_id | string | | |
action_result.parameter.system_id | string | | |
action_result.data.\*.job_id | string | | |
action_result.data.\*.status | string | | |
action_result.data.\*.source | string | | |
action_result.data.\*.agent_id | string | | |
summary.total_objects | numeric | | 1 |
summary.total_objects_successful | numeric | | 1 |

## action: 'volume offline'

Take volume offline

Type: **generic** <br>
Read only: **False**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**volume_id** | required | Volume Id | string | |
**agent_id** | required | Agent Id | string | |
**system_id** | required | System Id | string | |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string | | success failure |
action_result.message | string | | |
action_result.parameter.volume_id | string | | |
action_result.parameter.agent_id | string | | |
action_result.parameter.system_id | string | | |
action_result.data.\*.job_id | string | | |
action_result.data.\*.status | string | | |
action_result.data.\*.source | string | | |
action_result.data.\*.agent_id | string | | |
summary.total_objects | numeric | | 1 |
summary.total_objects_successful | numeric | | 1 |

## action: 'volume online'

Take volume online

Type: **generic** <br>
Read only: **False**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**volume_id** | required | Volume Id | string | |
**agent_id** | required | Agent Id | string | |
**system_id** | required | System Id | string | |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string | | success failure |
action_result.message | string | | |
action_result.parameter.volume_id | string | | |
action_result.parameter.agent_id | string | | |
action_result.parameter.system_id | string | | |
action_result.data.\*.job_id | string | | |
action_result.data.\*.status | string | | |
action_result.data.\*.source | string | | |
action_result.data.\*.agent_id | string | | |
summary.total_objects | numeric | | 1 |
summary.total_objects_successful | numeric | | 1 |

## action: 'check job status'

Check the status of an enrichment job

Type: **investigate** <br>
Read only: **True**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**job_id** | required | Job Id | string | |
**agent_id** | required | Agent Id | string | |
**source** | required | Source | string | |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string | | success failure |
action_result.message | string | | |
action_result.parameter.job_id | string | | |
action_result.parameter.agent_id | string | | |
action_result.parameter.source | string | | |
action_result.data.\*.job_id | string | | |
action_result.data.\*.source | string | | |
action_result.data.\*.status | string | | |
action_result.data.\*.records.\*.system_id | string | | |
action_result.data.\*.records.\*.ip_address | string | | |
action_result.data.\*.records.\*.lif_type | string | | |
action_result.data.\*.records.\*.scope | string | | |
action_result.data.\*.records.\*.svm | string | | |
action_result.data.\*.records.\*.agent_id | string | | |
action_result.data.\*.message | string | | |
summary.total_objects | numeric | | 1 |
summary.total_objects_successful | numeric | | 1 |

## action: 'block user'

Block user from accessing resources protected by Ransomware Resilience

Type: **contain** <br>
Read only: **False**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**user_id** | required | User ID to block | string | |
**user_ips** | required | Client IPs to block (required for NFS; optional for CIFS). Comma-separated. | string | |
**duration** | required | Block duration - permanent or hours (1, 2, 4, 8, 12, 24) | string | |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string | | success failure |
action_result.message | string | | |
action_result.parameter.user_id | string | | |
action_result.parameter.user_ips | string | | |
action_result.parameter.duration | string | | |
action_result.data.\*.message | string | | |
summary.total_objects | numeric | | 1 |
summary.total_objects_successful | numeric | | 1 |

______________________________________________________________________

Auto-generated Splunk SOAR Connector documentation.

Copyright 2026 Splunk Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
