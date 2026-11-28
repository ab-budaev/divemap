import uuid
from typing import Annotated

import fastapi
from pydantic import BaseModel, Field, StringConstraints

from api.dependencies import get_spot_repository
from application.spots import CreateSpot, ListSpots, SpotDTO
from domain.spots import SpotRepository

spots_router = fastapi.APIRouter(prefix="/spots", tags=["spots"])


class SpotCreateRequest(BaseModel):
    name: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
    description: str | None = None
    lat: float = Field(ge=-90, le=90)
    lng: float = Field(ge=-180, le=180)


class SpotResponse(BaseModel):
    id: uuid.UUID
    name: str
    description: str | None
    lat: float
    lng: float


@spots_router.get(
    "",
    response_model=list[SpotResponse],
    summary="Список мест погружений",
)
def list_spots(spots: SpotRepository = fastapi.Depends(get_spot_repository)) -> list[SpotDTO]:
    return ListSpots(spots).execute()


@spots_router.post(
    "",
    response_model=SpotResponse,
    status_code=fastapi.status.HTTP_201_CREATED,
    summary="Создание места погружения",
)
def create_spot(
    payload: SpotCreateRequest,
    spots: SpotRepository = fastapi.Depends(get_spot_repository),
) -> SpotDTO:
    return CreateSpot(spots).execute(
        name=payload.name,
        description=payload.description,
        lat=payload.lat,
        lng=payload.lng,
    )
