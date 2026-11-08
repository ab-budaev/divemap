import uuid
from datetime import datetime
from typing import Protocol

from pydantic import BaseModel, ConfigDict


class User(BaseModel):
    model_config = ConfigDict(frozen=True)

    id: uuid.UUID
    name: str
    created_at: datetime
    updated_at: datetime


class UserRepository(Protocol):
    def get_first(self) -> User | None: ...
