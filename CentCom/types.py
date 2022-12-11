from __future__ import annotations  # Required so we can reference BanData in its own staticmethod
from typing import Optional
from enum import Enum
from dataclasses import dataclass
import json

from requests import Response


class RoleplayLevel(Enum):
    Unknown = 0
    Low = 1
    Medium = 2
    High = 3


class BanType(Enum):
    Server = 0
    Job = 1


@dataclass(repr=True, frozen=True)
class BanData:
    id: int = -1
    sourceID: int = -1
    sourceName: Optional[str] = None
    sourceRoleplayLevel: RoleplayLevel = RoleplayLevel.Unknown
    type: BanType = BanType.Server
    cKey: Optional[str] = None
    bannedOn: str = "ERROR"
    bannedBy: Optional[str] = None
    reason: Optional[str] = None
    expires: Optional[str] = None
    unbannedBy: Optional[str] = None
    banID: Optional[str] = None
    jobs: Optional[list[str]] = None
    banAttributes: Optional[list[str]] = None
    active: bool = False

    @staticmethod
    def from_response(r: Response) -> list[BanData]:
        return r.json(object_hook=lambda d: BanData(**d))

    @staticmethod
    def from_json_string(r: str) -> list[BanData]:
        return json.loads(r, object_hook=lambda d: BanData(**d))
