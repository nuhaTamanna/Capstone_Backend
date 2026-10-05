from pydantic import BaseModel
from app.schemas.alert import Alert
from app.schemas.prediction import Status


class AreaSummary(BaseModel):
    name: str
    traffic_status: Status
    pollution_status: Status
    severity: Status


class AuthorityDashboard(BaseModel):
    monitored_areas: int
    active_alerts: int
    high_severity_areas: int
    critical_areas: int
    areas: list[AreaSummary]
    recent_alerts: list[Alert]
