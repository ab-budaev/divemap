from application.spots import ListSpots, SpotDTO
from domain.spots import Spot
from tests.stubs import StubSpotRepository


def test_returns_spot_dtos(spot: Spot, spot_repository: StubSpotRepository) -> None:
    result = ListSpots(spot_repository).execute()

    assert result == [
        SpotDTO(
            id=spot.id,
            name=spot.name,
            description=spot.description,
            lat=spot.lat,
            lng=spot.lng,
        )
    ]


def test_returns_empty_list_when_no_spots(empty_spot_repository: StubSpotRepository) -> None:
    result = ListSpots(empty_spot_repository).execute()

    assert result == []
