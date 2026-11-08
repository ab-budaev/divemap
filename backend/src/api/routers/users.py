import uuid

import fastapi
from pydantic import BaseModel

from api.dependencies import get_user_repository
from application.users import CurrentUserDTO, GetCurrentUser
from domain.users import UserRepository

users_router = fastapi.APIRouter(prefix="/users", tags=["users"])


class UserResponse(BaseModel):
    id: uuid.UUID
    name: str


def get_current_user(users: UserRepository = fastapi.Depends(get_user_repository)) -> CurrentUserDTO | None:
    return GetCurrentUser(users).execute()


@users_router.get(
    "/me",
    response_model=UserResponse,
    summary="Информация о текущем пользователе",
)
def read_current_user(current: CurrentUserDTO | None = fastapi.Depends(get_current_user)) -> UserResponse:
    if current is None:
        raise fastapi.HTTPException(status_code=404, detail="Текущий пользователь не найден")
    return UserResponse(id=current.id, name=current.name)
