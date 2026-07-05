# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from dataclasses import dataclass

from synerise_sdk.dto import DTO


@dataclass
class Profile(DTO):
    email: str
    phone: str | None = None
    area_code: str | None = None
    agreements: dict | None = None
    uuid: str | None = None


@dataclass
class ClientProfileEvent(DTO):
    customId: str | None = None
    id: str | None = None
    uuid: str | None = None
    email: str | None = None


@dataclass
class ProfileEvent(DTO):
    action: str
    client: ClientProfileEvent
    label: str | None = None
    time: str | None = None
    eventSalt: str | None = None
    params: str | None = None
