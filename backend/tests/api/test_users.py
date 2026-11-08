from fastapi.testclient import TestClient

from domain.users import User
from tests.stubs import StubUserRepository


def test_users_me_returns_current_user(
    client: TestClient,
    user_repository: StubUserRepository,
    user: User,
) -> None:
    response = client.get("/users/me")

    assert response.status_code == 200
    assert response.json() == {"id": str(user.id), "name": user.name}


def test_users_me_returns_404_when_user_not_found(
    client: TestClient,
    empty_user_repository: StubUserRepository,
) -> None:
    response = client.get("/users/me")

    assert response.status_code == 404
    assert response.json() == {"detail": "Текущий пользователь не найден"}
