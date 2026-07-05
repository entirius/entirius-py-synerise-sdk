# synerise-sdk

Synerise CDP SDK — workspace authentication and customer profile sync over the Synerise REST API.

## Installation

```shell
pip install entirius-py-synerise-sdk
```

## Usage

```python
from synerise_sdk import SyneriseClient
from synerise_sdk.dto.profile import Profile

client = SyneriseClient(subdomain="https://api.synerise.com", api_key="...")
client.get_workspace_token()
client.get_profile_create(Profile(email="user@example.com", uuid="...").asdict())
```

## Development

```shell
make install     # sync dependencies (uv)
make check       # lint + format check (ruff)
make test        # test suite (pytest) — integration test skipped without SYNERISE_API_KEY
```

Development and agent instructions: [AGENTS.md](AGENTS.md).

## License

Mozilla Public License 2.0 — see [LICENSE](LICENSE).
