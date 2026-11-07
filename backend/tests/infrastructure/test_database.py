"""Тесты infrastructure-слоя: движок, сессия и проверка живости соединения."""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from infrastructure.database import create_session_factory, ping


def test_session_factory_creates_session() -> None:
    engine = create_engine("sqlite+pysqlite:///:memory:")
    session_factory = create_session_factory(engine)

    with session_factory() as session:
        assert isinstance(session, Session)


def test_ping_select_one_succeeds() -> None:
    engine = create_engine("sqlite+pysqlite:///:memory:")
    session_factory = create_session_factory(engine)

    with session_factory() as session:
        assert ping(session) is True
