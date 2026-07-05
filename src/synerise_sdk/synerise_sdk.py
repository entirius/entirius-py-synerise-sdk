# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import json
from typing import Any

import requests

from synerise_sdk.dto.profile import Profile, ProfileEvent
from synerise_sdk.validators.response import validate_synerise_response, validate_token


class SyneriseClient:
    subdomain: str
    api_key: str

    def __init__(self, subdomain: str, api_key: str) -> None:
        self.subdomain = subdomain
        self.api_key = api_key

    @classmethod
    def from_user_com_api(cls, record):
        return cls(record.subdomain, record.api_key)

    @property
    def base_headers(self) -> dict:
        return {"content-type": "application/json"}

    @property
    def base_url(self) -> str:
        return f"{self.subdomain}"

    def make_resource_url(self, resource: str) -> str:
        return f"{self.base_url}{resource}"

    def get_workspace_token(self) -> dict:
        """
        Create and return token.
        """
        payload = {"apiKey": f"{self.api_key}"}
        response = requests.post(
            f"{self.make_resource_url('/uauth/v2/auth/login/profile')}", json=payload, headers=self.base_headers
        )
        validate_synerise_response(response)
        response_body = response.json()
        if not validate_token(response_body):
            raise ConnectionError("Synerise Connection error")
        data = response.json()["token"]
        return data

    def add_profile_to_event(self, final_body: ProfileEvent):
        token = self.get_workspace_token()
        base_headers_profile_post = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Api-Version": "4.4",
            "Authorization": f"Bearer {token}",
        }
        payload = json.dumps(final_body)
        url = self.make_resource_url("/v4/events/custom")
        response = requests.post(url, data=payload, headers=base_headers_profile_post)

        try:
            data = response.json()
        except Exception:
            data = response.text

        if not isinstance(data, str) and data.get("error", None) is not None:
            msg = response.json().get("message")
            status_code = response.status_code
        else:
            msg = "Profile successfully added to event form.submit"
            status_code = response.status_code

        return msg, status_code

    def get_profile_create(self, final_body: Profile) -> tuple[str, Any]:
        """
        Create profile on synerise
        """

        token = self.get_workspace_token()
        base_headers_profile_post = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Api-Version": "4.4",
            "Authorization": f"Bearer {token}",
        }

        payload = json.dumps(final_body)
        url = self.make_resource_url("/v4/clients")
        response = requests.post(url, data=payload, headers=base_headers_profile_post)
        try:
            data = response.json()
        except Exception:
            data = response.text

        if data != "":
            msg = response.json().get("error")
            status_code = response.status_code
        else:
            msg = "Profile successfully added/updated"
            status_code = response.status_code

        return msg, status_code
