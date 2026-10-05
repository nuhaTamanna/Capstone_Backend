from datetime import datetime, timezone

from app.data.india_geography import cities_for, divisions
from app.schemas.map import MapLocation


# Viewport centres are representative prototype map positions, not live sensor
# coordinates. Real town names stay in india_geography.json.
STATE_CENTRES = {
    "Andhra Pradesh": (15.9129, 79.7400), "Arunachal Pradesh": (28.2180, 94.7278), "Assam": (26.2006, 92.9376), "Bihar": (25.0961, 85.3131), "Chhattisgarh": (21.2787, 81.8661), "Goa": (15.2993, 74.1240), "Gujarat": (22.2587, 71.1924), "Haryana": (29.0588, 76.0856), "Himachal Pradesh": (31.1048, 77.1734), "Jharkhand": (23.6102, 85.2799), "Karnataka": (15.3173, 75.7139), "Kerala": (10.8505, 76.2711), "Madhya Pradesh": (22.9734, 78.6569), "Maharashtra": (19.7515, 75.7139), "Manipur": (24.6637, 93.9063), "Meghalaya": (25.4670, 91.3662), "Mizoram": (23.1645, 92.9376), "Nagaland": (26.1584, 94.5624), "Odisha": (20.9517, 85.0985), "Punjab": (31.1471, 75.3412), "Rajasthan": (27.0238, 74.2179), "Sikkim": (27.5330, 88.5122), "Tamil Nadu": (11.1271, 78.6569), "Telangana": (18.1124, 79.0193), "Tripura": (23.9408, 91.9882), "Uttar Pradesh": (26.8467, 80.9462), "Uttarakhand": (30.0668, 79.0193), "West Bengal": (22.9868, 87.8550), "Andaman and Nicobar Islands": (11.7401, 92.6586), "Chandigarh": (30.7333, 76.7794), "Dadra and Nagar Haveli and Daman and Diu": (20.1809, 73.0169), "Delhi": (28.7041, 77.1025), "Jammu and Kashmir": (33.7782, 76.5762), "Ladakh": (34.1526, 77.5771), "Lakshadweep": (10.5667, 72.6417), "Puducherry": (11.9416, 79.8083),
}
CONDITIONS = [("Critical", 14, 158, "Unhealthy"), ("High", 22, 131, "Unhealthy for sensitive groups"), ("Moderate", 31, 88, "Moderate"), ("Low", 42, 58, "Good")]


def _location(state: str, locality: str, index: int) -> MapLocation:
    latitude, longitude = STATE_CENTRES[state]
    # Separate markers enough to keep each selected locality visible in the demo.
    latitude += ((index % 9) - 4) * 0.045
    longitude += ((index // 9 % 9) - 4) * 0.045
    traffic_level, average_speed, aqi, pollution_category = CONDITIONS[index % len(CONDITIONS)]
    return MapLocation(location_id=f"india-{state}-{locality}".lower().replace(" ", "-"), name=f"{locality} monitoring area", latitude=latitude, longitude=longitude, traffic_level=traffic_level, average_speed=average_speed, aqi=aqi, pollution_category=pollution_category, alert_id=index if traffic_level in {"Critical", "High"} else None, updated_at=datetime.now(timezone.utc), continent="Asia", country="India", state=state, locality=locality)


def prototype_map_locations(state: str | None = None, locality: str | None = None) -> list[MapLocation]:
    """Return India-only representative map records for the requested scope."""
    if state:
        cities = cities_for(state)
        if locality:
            cities = [city for city in cities if city == locality]
        return [_location(state, city, index) for index, city in enumerate(cities)]
    return [_location(division["name"], division["cities"][0], index) for index, division in enumerate(divisions())]
