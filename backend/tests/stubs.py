from domain.spots import Spot
from domain.users import User


class StubUserRepository:
    def __init__(self, user: User | None) -> None:
        self._user = user

    def get_first(self) -> User | None:
        return self._user


class StubSpotRepository:
    def __init__(self, spots: list[Spot]) -> None:
        self._spots = spots

    def get_all(self) -> list[Spot]:
        return self._spots
