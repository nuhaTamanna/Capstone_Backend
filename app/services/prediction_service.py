from datetime import datetime
from app.data.prototype_data import CONTRIBUTIONS
from app.schemas.prediction import PredictionResponse


class PrototypePredictionService:
    """Replace with an ML-backed service later; retain this response contract."""
    hotspots = ("kollupitiya", "rajagiriya", "borella", "fort", "maradana")

    def predict_location(self, location: str, when: datetime | None) -> PredictionResponse:
        return self._build(location, when)

    def predict_route(self, origin: str, destination: str, when: datetime | None) -> PredictionResponse:
        return self._build(f"{origin} to {destination}", when).model_copy(update={"route_summary": f"{origin} → {destination}"})

    def _build(self, subject: str, when: datetime | None) -> PredictionResponse:
        target = when or datetime.now()
        peak = target.hour in {7, 8, 9, 17, 18, 19}
        hotspot = any(term in subject.lower() for term in self.hotspots)
        if peak and hotspot: traffic, pollution, severity, confidence = "Critical", "High", "Critical", 91
        elif peak or hotspot: traffic, pollution, severity, confidence = "High", "Moderate", "High", 86
        else: traffic, pollution, severity, confidence = "Moderate", "Low", "Moderate", 76
        demand = "Peak-hour travel demand" if peak else "Typical daytime travel demand"
        return PredictionResponse(location=subject, traffic_status=traffic, pollution_status=pollution, severity=severity, confidence=confidence, prediction_time=target.strftime("%d %b %Y, %I:%M %p"), main_factors=[demand, "Historical congestion pattern", "Weather conditions"], feature_contributions=CONTRIBUTIONS, explanation=f"{traffic} traffic is predicted for {subject}. The result is driven by {demand.lower()} and recurring traffic patterns. Pollution is expected to remain {pollution.lower()} as traffic conditions influence local emissions.")


prediction_service = PrototypePredictionService()
