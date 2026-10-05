from app.schemas.alert import Alert
from app.schemas.prediction import FeatureContribution

CONTRIBUTIONS = [
    FeatureContribution(feature="Peak-hour travel demand", contribution=0.42),
    FeatureContribution(feature="Historical congestion pattern", contribution=0.31),
    FeatureContribution(feature="Weather conditions", contribution=0.14),
    FeatureContribution(feature="Local air-quality baseline", contribution=0.13),
]

ALERTS: list[Alert] = [
    Alert(id=1, area="Kollupitiya Junction", prediction="Evening congestion expected", severity="Critical", prediction_time="Next 45 minutes", confidence=91, main_factors=["Peak-hour travel demand", "Historical congestion pattern", "Road works"], status="New", traffic_status="Critical", pollution_status="High", feature_contributions=CONTRIBUTIONS, explanation="Traffic demand near Kollupitiya Junction is likely to exceed normal road capacity during the evening peak. Pollution is expected to rise as slower traffic increases emissions."),
    Alert(id=2, area="Rajagiriya Flyover", prediction="High traffic build-up expected", severity="High", prediction_time="Next 60 minutes", confidence=86, main_factors=["Peak-hour travel demand", "Weather conditions", "School dismissal period"], status="New", traffic_status="High", pollution_status="Moderate", feature_contributions=CONTRIBUTIONS, explanation="A sustained build-up is predicted around Rajagiriya as regular peak-hour demand combines with local trip activity."),
    Alert(id=3, area="Borella Junction", prediction="Air-quality deterioration expected", severity="High", prediction_time="Next 90 minutes", confidence=82, main_factors=["Historical congestion pattern", "Local air-quality baseline", "Low wind conditions"], status="Acknowledged", traffic_status="High", pollution_status="High", feature_contributions=CONTRIBUTIONS, explanation="Recurring congestion and the existing air-quality baseline indicate a higher likelihood of elevated pollution around Borella."),
]
