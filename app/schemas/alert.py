from typing import Literal
from pydantic import BaseModel
from app.schemas.prediction import FeatureContribution, Status

AlertStatus = Literal["New", "Acknowledged"]


class Alert(BaseModel):
    id: int
    area: str
    prediction: str
    severity: Status
    prediction_time: str
    confidence: int
    main_factors: list[str]
    status: AlertStatus
    traffic_status: Status
    pollution_status: Status
    feature_contributions: list[FeatureContribution]
    explanation: str
