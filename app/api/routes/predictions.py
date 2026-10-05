from fastapi import APIRouter
from app.schemas.prediction import LocationPredictionRequest, PredictionResponse, RoutePredictionRequest
from app.services.prediction_service import prediction_service

router = APIRouter(prefix="/predictions", tags=["predictions"])


@router.post("/location", response_model=PredictionResponse)
def location_prediction(payload: LocationPredictionRequest):
    return prediction_service.predict_location(payload.location, payload.datetime)


@router.post("/route", response_model=PredictionResponse)
def route_prediction(payload: RoutePredictionRequest):
    return prediction_service.predict_route(payload.origin, payload.destination, payload.datetime)
