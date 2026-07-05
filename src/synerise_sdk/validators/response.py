# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from requests import Response


def validate_synerise_response(response: Response) -> (bool, dict):
    try:
        response_body = response.json()
    except Exception:
        response_body = response.text

    if response.status_code == 200:
        return True, response_body

    if response.status_code == 201:
        return True, response_body

    if response.status_code == 202:
        return True, response_body

    if response.status_code == 302:
        return True, response_body

    if response.status_code == 401:
        msg_error = response_body["message"]
        raise ConnectionError(msg_error)
    return False, response_body


def validate_token(response_body: dict) -> bool:
    if "token" in response_body:
        return True
    return False
