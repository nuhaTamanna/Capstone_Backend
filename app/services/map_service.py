from app.data.india_geography import cities_for, divisions
from app.data.map_data import prototype_map_locations
from app.schemas.map import GeographyOption, IntelligenceSummary, MapOverview, MapStatus, MapViewport, TrendPoint
from app.services.dashboard_service import dashboard_service


class MapIntelligenceService:
    """Maps prototype geospatial data into a stable contract for future live feeds."""

    def locations(self, continent: str | None = None, country: str | None = None, state: str | None = None, locality: str | None = None):
        # India is intentionally the fixed geographic scope for this prototype.
        if continent and continent != "Asia" or country and country != "India":
            return []
        return prototype_map_locations(state, locality)

    def geographies(self) -> list[GeographyOption]:
        options: list[GeographyOption] = []
        for division in divisions():
            state = division["name"]
            for index, locality in enumerate(cities_for(state)):
                location = prototype_map_locations(state, locality)[0]
                options.append(GeographyOption(continent="Asia", country="India", state=state, locality=locality, viewport=MapViewport(latitude=location.latitude, longitude=location.longitude, zoom=12)))
        return options

    def viewport(self, locations) -> MapViewport:
        if not locations:
            return MapViewport(latitude=22.9734, longitude=78.6569, zoom=5)
        if len(locations) == 1:
            return MapViewport(latitude=locations[0].latitude, longitude=locations[0].longitude, zoom=13)
        return MapViewport(latitude=sum(item.latitude for item in locations) / len(locations), longitude=sum(item.longitude for item in locations) / len(locations), zoom=8 if len(locations) > 3 else 10)

    def status(self, locations=None) -> MapStatus:
        dashboard = dashboard_service.authority_dashboard()
        locations = self.locations() if locations is None else locations
        if not locations:
            return MapStatus(overall_traffic="Low", average_aqi=0, active_alerts=0, critical_areas=0)
        order = {"Low": 1, "Moderate": 2, "High": 3, "Critical": 4}
        overall = max(locations, key=lambda item: order[item.traffic_level]).traffic_level
        return MapStatus(overall_traffic=overall, average_aqi=round(sum(item.aqi for item in locations) / len(locations)), active_alerts=sum(item.alert_id is not None for item in locations), critical_areas=sum(item.traffic_level == "Critical" for item in locations) if len(locations) != len(self.locations()) else dashboard.critical_areas)

    def overview(self, continent: str | None = None, country: str | None = None, state: str | None = None, locality: str | None = None) -> MapOverview:
        locations = self.locations(continent, country, state, locality)
        return MapOverview(status=self.status(locations), locations=locations, traffic_trend=[TrendPoint(label=label, value=value) for label, value in [("08:00", 58), ("11:00", 42), ("14:00", 55), ("17:00", 78), ("Now", 86)]], pollution_trend=[TrendPoint(label=label, value=value) for label, value in [("08:00", 104), ("11:00", 96), ("14:00", 110), ("17:00", 132), ("Now", 137)]], prediction_summary=IntelligenceSummary(prediction="High congestion expected near monitored hotspots", confidence=88, primary_factor="Peak-hour travel demand"), explainability_summary=IntelligenceSummary(prediction="Traffic demand is the dominant contributor", confidence=91, primary_factor="Historical congestion pattern"), viewport=self.viewport(locations))


map_intelligence_service = MapIntelligenceService()
