"""Infrastructure: подключение к PostgreSQL через синхронный SQLAlchemy 2.0.

- `engine` — глобальный движок, конфигурируется из `AppSettings.database_url`
- `SessionLocal` — фабрика сессий для работы с БД
- `Base` — базовый класс ORM-моделей (декларативный стиль SQLAlchemy 2.0)
- `ping` — служебная проверка живости соединения (запрос `SELECT 1`)
"""

from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from settings import AppSettings


class Base(DeclarativeBase):
    """Базовый класс всех ORM-моделей приложения."""


def create_db_engine(database_url: str) -> Engine:
    """Создаёт синхронный движок SQLAlchemy по DSN.

    Для CRUD одного пользователя достаточен пул по умолчанию; FastAPI
    исполняет синхронные вызовы в threadpool.
    """
    return create_engine(database_url, pool_pre_ping=True)


def create_session_factory(engine: Engine) -> sessionmaker[Session]:
    """Создаёт фабрику сессий для переданного движка."""
    return sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


def build_session_factory(settings: AppSettings) -> sessionmaker[Session]:
    """Собирает фабрику сессий из настроек приложения."""
    return create_session_factory(create_db_engine(settings.database_url))


def ping(session: Session) -> bool:
    """Проверяет живость соединения запросом `SELECT 1`."""
    session.execute(text("SELECT 1"))
    return True
