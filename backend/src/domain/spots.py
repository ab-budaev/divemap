import uuid
from datetime import datetime
from typing import Protocol

from pydantic import BaseModel, ConfigDict


class Spot(BaseModel):
    model_config = ConfigDict(frozen=True)

    id: uuid.UUID
    name: str
    description: str | None
    lat: float
    lng: float
    created_at: datetime
    updated_at: datetime


class SpotRepository(Protocol):
    def get_all(self) -> list[Spot]: ...
