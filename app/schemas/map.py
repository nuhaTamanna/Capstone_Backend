from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field

from app.schemas.prediction import Status

PollutionCategory = Literal["Good", "Moderate", "Unhealthy for sensitive groups", "Unhealthy"]


class MapLocation(BaseModel):
    location_id: str
    name: str
    latitude: float
    longitude: float
    traffic_level: Status
    average_speed: int = Field(ge=0)
    aqi: int = Field(ge=0)
    pollution_category: PollutionCategory
    alert_id: int | None = None
    updated_at: datetime
    continent: str
    country: str
    state: str
    locality: str


class MapViewport(BaseModel):
    latitude: float
    longitude: float
    zoom: int = Field(ge=2, le=18)


class GeographyOption(BaseModel):
    continent: str
    country: str
    state: str
    locality: str
    viewport: MapViewport


class MapStatus(BaseModel):
    overall_traffic: Status
    average_aqi: int
    active_alerts: int
    critical_areas: int


class TrendPoint(BaseModel):
    label: str
    value: int


class IntelligenceSummary(BaseModel):
    prediction: str
    confidence: int
    primary_factor: str


class MapOverview(BaseModel):
    status: MapStatus
    locations: list[MapLocation]
    traffic_trend: list[TrendPoint]
    pollution_trend: list[TrendPoint]
    prediction_summary: IntelligenceSummary
    explainability_summary: IntelligenceSummary
    viewport: MapViewport
