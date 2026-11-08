import os

os.environ["OTEL_SDK_DISABLED"] = "true"
os.environ["DATABASE_URL"] = "postgresql+psycopg://user:pass@localhost:5432/test_db"

import uuid
from datetime import UTC, datetime

import fastapi
import pytest
from fastapi.testclient import TestClient

from domain.users import User
from main import app as _app
from tests.stubs import StubUserRepository


@pytest.fixture
def app() -> fastapi.FastAPI:
    return _app


@pytest.fixture
def test_client(app: fastapi.FastAPI) -> TestClient:
    return TestClient(app=app)


@pytest.fixture
def test_client_raise_exceptions(app: fastapi.FastAPI) -> TestClient:
    return TestClient(app=app, raise_server_exceptions=True)


@pytest.fixture
def user() -> User:
    now = datetime.now(tz=UTC)
    return User(id=uuid.uuid4(), name="budaev", created_at=now, updated_at=now)


@pytest.fixture
def user_repository(user: User) -> StubUserRepository:
    return StubUserRepository(user)


@pytest.fixture
def empty_user_repository() -> StubUserRepository:
    return StubUserRepository(None)
