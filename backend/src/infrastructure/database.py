from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from settings import AppSettings


class Base(DeclarativeBase):
    pass


def create_db_engine(database_url: str) -> Engine:
    return create_engine(database_url, pool_pre_ping=True)


def create_session_factory(engine: Engine) -> sessionmaker[Session]:
    return sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


def build_session_factory(settings: AppSettings) -> sessionmaker[Session]:
    return create_session_factory(create_db_engine(settings.database_url))


def ping(session: Session) -> bool:
    session.execute(text("SELECT 1"))
    return True
