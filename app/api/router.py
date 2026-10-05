from fastapi import APIRouter
from app.api.routes import alerts, dashboard, map, predictions, saved_routes

api_router = APIRouter()
api_router.include_router(predictions.router)
api_router.include_router(saved_routes.router)
api_router.include_router(alerts.router)
api_router.include_router(dashboard.router)
api_router.include_router(map.router)
