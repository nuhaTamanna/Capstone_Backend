from fastapi import APIRouter

from app.schemas.map import GeographyOption, MapLocation, MapOverview, MapStatus
from app.services.map_service import map_intelligence_service

router = APIRouter(prefix="/map", tags=["urban intelligence map"])


@router.get("/overview", response_model=MapOverview)
def map_overview(continent: str | None = None, country: str | None = None, state: str | None = None, locality: str | None = None): return map_intelligence_service.overview(continent, country, state, locality)


@router.get("/geographies", response_model=list[GeographyOption])
def map_geographies(): return map_intelligence_service.geographies()


@router.get("/status", response_model=MapStatus)
def map_status(): return map_intelligence_service.status()


@router.get("/locations", response_model=list[MapLocation])
def map_locations(): return map_intelligence_service.locations()


@router.get("/traffic", response_model=list[MapLocation])
def map_traffic(): return map_intelligence_service.locations()


@router.get("/pollution", response_model=list[MapLocation])
def map_pollution(): return map_intelligence_service.locations()
