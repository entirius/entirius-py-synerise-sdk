# entirius-py-synerise-sdk

A Python client for the Synerise customer data platform REST API, part of Entirius, the open-source modular ecommerce platform.
It authenticates a workspace, creates customer profiles and sends custom events behind one `SyneriseClient` class.

[![PyPI](https://img.shields.io/pypi/v/entirius-py-synerise-sdk.svg)](https://pypi.org/project/entirius-py-synerise-sdk/)
[![Python](https://img.shields.io/pypi/pyversions/entirius-py-synerise-sdk.svg)](https://pypi.org/project/entirius-py-synerise-sdk/)
[![License: MPL-2.0](https://img.shields.io/badge/license-MPL--2.0-blue.svg)](https://github.com/entirius/entirius-py-synerise-sdk/blob/develop/LICENSE)

## What it does

- Authenticates a workspace with its API key and returns the token (`get_workspace_token()`).
- Creates a customer profile (`get_profile_create()`, payload from the `Profile` DTO).
- Sends a custom event for a profile (`add_profile_to_event()`, payload from the `ProfileEvent` DTO).
- Works against any Synerise API host: the base URL is the `subdomain` argument.

## Installation

```shell
uv add entirius-py-synerise-sdk
pip install entirius-py-synerise-sdk
```

The import name is `synerise_sdk`.

## Quick start

```python
from synerise_sdk import SyneriseClient
from synerise_sdk.dto.profile import Profile

client = SyneriseClient(subdomain="https://api.synerise.com", api_key="...")
client.get_workspace_token()
client.get_profile_create(Profile(email="user@example.com", uuid="...").asdict())
```

## Requirements

- Python 3.11 or newer.
- `requests` (installed as a dependency).
- A Synerise workspace (API key).

## Documentation

- Entirius documentation: https://docs.entirius.com/
- Changelog: https://github.com/entirius/entirius-py-synerise-sdk/blob/develop/CHANGELOG.md

## Part of Entirius

This SDK is one of the marketing integration clients used by the Entirius backend service (Volkanos).

- Backend service: https://github.com/entirius/entirius-service-volkanos
- Docker harness: https://github.com/entirius/entirius-zeno
- Sibling marketing SDKs: https://github.com/entirius/entirius-py-edrone-sdk, https://github.com/entirius/entirius-py-get-response-sdk, https://github.com/entirius/entirius-py-salesmanago-sdk

## Development

```shell
make install     # sync dependencies (uv)
make check       # lint + format check (ruff)
make test        # test suite (pytest); the integration test is skipped without SYNERISE_API_KEY
```

Development and agent instructions: https://github.com/entirius/entirius-py-synerise-sdk/blob/develop/AGENTS.md

## License

Mozilla Public License 2.0 (MPL-2.0) — see https://github.com/entirius/entirius-py-synerise-sdk/blob/develop/LICENSE.
