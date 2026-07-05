# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import os

import pytest

from synerise_sdk import SyneriseClient
from synerise_sdk.dto.profile import Profile

# Generate an API key at https://app.synerise.com/settings/apikeys
API_KEY_SYNERISE = os.environ.get("SYNERISE_API_KEY")
DOMAIN_SYNERISE = "https://api.synerise.com"

pytestmark = pytest.mark.skipif(not API_KEY_SYNERISE, reason="Synerise credentials not set (SYNERISE_API_KEY env var)")


def test_get_workspace_token():
    synerise_client = SyneriseClient(
        subdomain=DOMAIN_SYNERISE,
        api_key=API_KEY_SYNERISE,
    )
    token = synerise_client.get_workspace_token()
    assert isinstance(token, str)


def test_create_synerise_profile():
    synerise_client = SyneriseClient(
        subdomain=DOMAIN_SYNERISE,
        api_key=API_KEY_SYNERISE,
    )
    synerise_client.get_workspace_token()
    profile = Profile(
        email="user@example.com",
        area_code="48",
        phone="123123123",
        agreements={"email": "false", "sms": "true", "push": "true"},
        uuid="944ed506-c052-41b4-819c-2de7fa95b007",
    )
    profile = profile.asdict()
    msg, status_code = synerise_client.get_profile_create(profile)
    assert isinstance(msg, str)
    assert isinstance(status_code, int)
