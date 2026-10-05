from app.schemas.dashboard import AreaSummary, AuthorityDashboard
from app.services.alert_service import alert_service


class DashboardService:
    def authority_dashboard(self) -> AuthorityDashboard:
        alerts = alert_service.list_alerts()
        areas = [AreaSummary(name=a.area, traffic_status=a.traffic_status, pollution_status=a.pollution_status, severity=a.severity) for a in alerts]
        return AuthorityDashboard(monitored_areas=len(areas), active_alerts=sum(a.status == "New" for a in alerts), high_severity_areas=sum(a.severity in {"High", "Critical"} for a in alerts), critical_areas=sum(a.severity == "Critical" for a in alerts), areas=areas, recent_alerts=alerts[:2])


dashboard_service = DashboardService()
