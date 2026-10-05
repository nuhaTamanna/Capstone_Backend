from fastapi import APIRouter, HTTPException
from app.schemas.alert import Alert
from app.services.alert_service import alert_service

router = APIRouter(prefix="/alerts", tags=["alerts"])


@router.get("", response_model=list[Alert])
def list_alerts(): return alert_service.list_alerts()


@router.get("/{alert_id}", response_model=Alert)
def get_alert(alert_id: int):
    alert = alert_service.get_alert(alert_id)
    if not alert: raise HTTPException(404, "Alert not found")
    return alert


@router.patch("/{alert_id}/acknowledge", response_model=Alert)
def acknowledge_alert(alert_id: int):
    alert = alert_service.acknowledge(alert_id)
    if not alert: raise HTTPException(404, "Alert not found")
    return alert
