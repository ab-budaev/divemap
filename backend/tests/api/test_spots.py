from fastapi.testclient import TestClient

from domain.spots import Spot
from tests.stubs import StubSpotRepository


def test_spots_returns_all_spots(
    client: TestClient,
    spot_repository: StubSpotRepository,
    spot: Spot,
) -> None:
    response = client.get("/spots")

    assert response.status_code == 200
    assert response.json() == [
        {
            "id": str(spot.id),
            "name": spot.name,
            "description": spot.description,
            "lat": spot.lat,
            "lng": spot.lng,
        }
    ]


def test_spots_returns_empty_list_when_no_spots(
    client: TestClient,
    empty_spot_repository: StubSpotRepository,
) -> None:
    response = client.get("/spots")

    assert response.status_code == 200
    assert response.json() == []
