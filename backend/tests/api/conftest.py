from collections.abc import Iterator

import fastapi
import pytest
from fastapi.testclient import TestClient

from api.dependencies import get_spot_repository, get_user_repository
from domain.spots import Spot
from domain.users import User
from tests.stubs import StubSpotRepository, StubUserRepository


@pytest.fixture
def client(app: fastapi.FastAPI) -> Iterator[TestClient]:
    with TestClient(app=app) as client:
        yield client
    app.dependency_overrides.clear()


@pytest.fixture
def user_repository(app: fastapi.FastAPI, user: User) -> StubUserRepository:
    repository = StubUserRepository(user)
    app.dependency_overrides[get_user_repository] = lambda: repository
    return repository


@pytest.fixture
def empty_user_repository(app: fastapi.FastAPI) -> StubUserRepository:
    repository = StubUserRepository(None)
    app.dependency_overrides[get_user_repository] = lambda: repository
    return repository


@pytest.fixture
def spot_repository(app: fastapi.FastAPI, spot: Spot) -> StubSpotRepository:
    repository = StubSpotRepository([spot])
    app.dependency_overrides[get_spot_repository] = lambda: repository
    return repository


@pytest.fixture
def empty_spot_repository(app: fastapi.FastAPI) -> StubSpotRepository:
    repository = StubSpotRepository([])
    app.dependency_overrides[get_spot_repository] = lambda: repository
    return repository
