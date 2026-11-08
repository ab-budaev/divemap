from application.users import CurrentUserDTO, GetCurrentUser
from domain.users import User
from tests.stubs import StubUserRepository


def test_returns_current_user_dto(user: User, user_repository: StubUserRepository) -> None:
    result = GetCurrentUser(user_repository).execute()

    assert result == CurrentUserDTO(id=user.id, name=user.name)


def test_returns_none_when_no_users(empty_user_repository: StubUserRepository) -> None:
    result = GetCurrentUser(empty_user_repository).execute()

    assert result is None
