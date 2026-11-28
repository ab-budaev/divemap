from application.spots import CreateSpot, ListSpots, SpotDTO
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


def test_creates_spot(empty_spot_repository: StubSpotRepository) -> None:
    result = CreateSpot(empty_spot_repository).execute(
        name="Новая точка",
        description=None,
        lat=27.915,
        lng=34.330,
    )

    assert result.name == "Новая точка"
    assert result.description is None
    assert result.lat == 27.915
    assert result.lng == 34.330

    created = empty_spot_repository.get_all()
    assert len(created) == 1
    assert created[0].id == result.id
    assert created[0].name == result.name
