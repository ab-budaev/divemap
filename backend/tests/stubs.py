import uuid
from datetime import UTC, datetime

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

    def create(self, name: str, description: str | None, lat: float, lng: float) -> Spot:
        now = datetime.now(tz=UTC)
        spot = Spot(
            id=uuid.uuid4(),
            name=name,
            description=description,
            lat=lat,
            lng=lng,
            created_at=now,
            updated_at=now,
        )
        self._spots.append(spot)
        return spot
