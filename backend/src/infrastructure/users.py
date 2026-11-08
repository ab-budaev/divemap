import uuid
from datetime import datetime

from sqlalchemy import DateTime, Text, func, select
from sqlalchemy.orm import Mapped, Session, mapped_column

from domain.users import User
from infrastructure.database import Base


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    def to_domain(self) -> User:
        return User(id=self.id, name=self.name, created_at=self.created_at, updated_at=self.updated_at)


class SqlAlchemyUserRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def get_first(self) -> User | None:
        model = self._session.scalars(select(UserModel).order_by(UserModel.created_at).limit(1)).first()
        return model.to_domain() if model is not None else None
