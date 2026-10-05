from app.data.prototype_data import ALERTS
from app.schemas.alert import Alert


class AlertService:
    def list_alerts(self) -> list[Alert]: return ALERTS
    def get_alert(self, alert_id: int) -> Alert | None: return next((a for a in ALERTS if a.id == alert_id), None)
    def acknowledge(self, alert_id: int) -> Alert | None:
        alert = self.get_alert(alert_id)
        if alert and alert.status == "New": ALERTS[ALERTS.index(alert)] = alert.model_copy(update={"status": "Acknowledged"})
        return self.get_alert(alert_id)


alert_service = AlertService()
