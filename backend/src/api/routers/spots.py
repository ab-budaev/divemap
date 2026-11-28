import uuid

import fastapi
from pydantic import BaseModel

from api.dependencies import get_spot_repository
from application.spots import ListSpots, SpotDTO
from domain.spots import SpotRepository

spots_router = fastapi.APIRouter(prefix="/spots", tags=["spots"])


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
