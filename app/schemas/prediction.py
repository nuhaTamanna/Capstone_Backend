from datetime import datetime as DateTime
from typing import Literal
from pydantic import BaseModel, Field

Status = Literal["Low", "Moderate", "High", "Critical"]


class FeatureContribution(BaseModel):
    feature: str
    contribution: float = Field(ge=0, le=1)


class LocationPredictionRequest(BaseModel):
    location: str = Field(min_length=2, max_length=120)
    datetime: DateTime | None = None


class RoutePredictionRequest(BaseModel):
    origin: str = Field(min_length=2, max_length=120)
    destination: str = Field(min_length=2, max_length=120)
    datetime: DateTime | None = None


class PredictionResponse(BaseModel):
    location: str
    traffic_status: Status
    pollution_status: Status
    severity: Status
    confidence: int = Field(ge=0, le=100)
    prediction_time: str
    main_factors: list[str]
    feature_contributions: list[FeatureContribution]
    explanation: str
    route_summary: str | None = None
