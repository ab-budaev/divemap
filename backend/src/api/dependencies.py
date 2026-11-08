from collections.abc import Iterator
from functools import lru_cache

import fastapi
from sqlalchemy.orm import Session, sessionmaker

from domain.users import UserRepository
from infrastructure.database import build_session_factory
from infrastructure.users import SqlAlchemyUserRepository
from settings import get_settings


@lru_cache(maxsize=1)
def _session_factory() -> sessionmaker[Session]:
    return build_session_factory(get_settings())


def get_db_session() -> Iterator[Session]:
    with _session_factory()() as session:
        yield session


def get_user_repository(session: Session = fastapi.Depends(get_db_session)) -> UserRepository:
    return SqlAlchemyUserRepository(session)
