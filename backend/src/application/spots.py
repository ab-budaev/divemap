import uuid

from pydantic import BaseModel, ConfigDict

from domain.spots import SpotRepository


class SpotDTO(BaseModel):
    model_config = ConfigDict(frozen=True)

    id: uuid.UUID
    name: str
    description: str | None
    lat: float
    lng: float


class ListSpots:
    def __init__(self, spots: SpotRepository) -> None:
        self._spots = spots

    def execute(self) -> list[SpotDTO]:
        return [
            SpotDTO(
                id=spot.id,
                name=spot.name,
                description=spot.description,
                lat=spot.lat,
                lng=spot.lng,
            )
            for spot in self._spots.get_all()
        ]


class CreateSpot:
    def __init__(self, spots: SpotRepository) -> None:
        self._spots = spots

    def execute(self, name: str, description: str | None, lat: float, lng: float) -> SpotDTO:
        spot = self._spots.create(name=name, description=description, lat=lat, lng=lng)
        return SpotDTO(
            id=spot.id,
            name=spot.name,
            description=spot.description,
            lat=spot.lat,
            lng=spot.lng,
        )
