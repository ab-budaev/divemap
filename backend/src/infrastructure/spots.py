import uuid
from datetime import datetime

from sqlalchemy import DateTime, Float, Text, func, select
from sqlalchemy.orm import Mapped, Session, mapped_column

from domain.spots import Spot
from infrastructure.database import Base


class SpotModel(Base):
    __tablename__ = "spots"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(Text, nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    lat: Mapped[float] = mapped_column(Float, nullable=False)
    lng: Mapped[float] = mapped_column(Float, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    def to_domain(self) -> Spot:
        return Spot(
            id=self.id,
            name=self.name,
            description=self.description,
            lat=self.lat,
            lng=self.lng,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )


class SqlAlchemySpotRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def get_all(self) -> list[Spot]:
        models = self._session.scalars(select(SpotModel).order_by(SpotModel.created_at)).all()
        return [model.to_domain() for model in models]

    def create(self, name: str, description: str | None, lat: float, lng: float) -> Spot:
        model = SpotModel(name=name, description=description, lat=lat, lng=lng)
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return model.to_domain()
