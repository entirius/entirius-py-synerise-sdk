# AGENTS.md

Synerise CDP REST API SDK — distribution `entirius-py-synerise-sdk`, import `synerise_sdk`.

## Commands

| Command | Meaning |
|---|---|
| `make install` | sync dependencies (uv, incl. extras) |
| `make check` | lint + format-check (ruff) |
| `make fix` | auto-fix lint + format |
| `make test` | test suite (pytest) |

## Conventions

- English only: code, docs, commits, branches, PRs.
- MPL-2.0: every non-trivial source file carries the license header (pre-commit inserts it).
- Toolchain: uv + ruff + hatchling + pytest; all config in `pyproject.toml`; `uv.lock` committed.
- Git flow: `master` (production) + `develop` (integration); changes land via PR; semver tag on `master`.
- Never rename the import package `synerise_sdk` — it is a public API contract.
- Default: do not commit — git is the user's call.
- No AI attribution in commits or PR descriptions.

## Architecture

- `src/synerise_sdk/synerise_sdk.py`: `SyneriseClient` authenticates the workspace, then creates customer profiles
  and sends custom events over the Synerise REST API.
- `dto/profile.py`: `Profile` and `ProfileEvent` request DTOs.
- `validators/`: response shape validation.
- The integration test hits the live Synerise API and is skipped unless `SYNERISE_API_KEY` is set.
