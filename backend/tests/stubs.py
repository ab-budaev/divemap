from domain.users import User


class StubUserRepository:
    def __init__(self, user: User | None) -> None:
        self._user = user

    def get_first(self) -> User | None:
        return self._user
