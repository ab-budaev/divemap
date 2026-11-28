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


def test_create_spot(client: TestClient, empty_spot_repository: StubSpotRepository) -> None:
    payload = {
        "name": "Байкал, Листвянка",
        "description": "Ледовые погружения.",
        "lat": 51.8461,
        "lng": 104.8722,
    }

    response = client.post("/spots", json=payload)

    assert response.status_code == 201
    body = response.json()
    assert body["id"]
    assert body["name"] == payload["name"]
    assert body["description"] == payload["description"]
    assert body["lat"] == payload["lat"]
    assert body["lng"] == payload["lng"]

    list_response = client.get("/spots")
    assert list_response.status_code == 200
    assert list_response.json() == [body]


def test_create_spot_without_description(client: TestClient, empty_spot_repository: StubSpotRepository) -> None:
    response = client.post("/spots", json={"name": "Новая точка", "lat": 27.915, "lng": 34.330})

    assert response.status_code == 201
    assert response.json()["description"] is None


def test_create_spot_rejects_blank_name(client: TestClient, empty_spot_repository: StubSpotRepository) -> None:
    response = client.post("/spots", json={"name": "   ", "lat": 27.915, "lng": 34.330})

    assert response.status_code == 422
    assert empty_spot_repository.get_all() == []


def test_create_spot_rejects_out_of_range_coordinates(
    client: TestClient,
    empty_spot_repository: StubSpotRepository,
) -> None:
    response = client.post("/spots", json={"name": "Точка", "lat": 91.0, "lng": 34.330})

    assert response.status_code == 422

    response = client.post("/spots", json={"name": "Точка", "lat": 27.915, "lng": -181.0})

    assert response.status_code == 422
    assert empty_spot_repository.get_all() == []
