import uuid

from pydantic import BaseModel, ConfigDict

from domain.users import UserRepository


class CurrentUserDTO(BaseModel):
    model_config = ConfigDict(frozen=True)

    id: uuid.UUID
    name: str


class GetCurrentUser:
    def __init__(self, users: UserRepository) -> None:
        self._users = users

    def execute(self) -> CurrentUserDTO | None:
        user = self._users.get_first()
        if user is None:
            return None
        return CurrentUserDTO(id=user.id, name=user.name)
