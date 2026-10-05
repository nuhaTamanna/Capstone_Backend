from fastapi import APIRouter, HTTPException, status
from app.schemas.route import SavedRoute, SavedRouteCreate
from app.services.route_service import saved_route_service

router = APIRouter(prefix="/saved-routes", tags=["saved routes"])


@router.get("", response_model=list[SavedRoute])
def list_saved_routes(): return saved_route_service.list_routes()


@router.post("", response_model=SavedRoute, status_code=status.HTTP_201_CREATED)
def create_saved_route(payload: SavedRouteCreate): return saved_route_service.create_route(payload)


@router.delete("/{route_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_saved_route(route_id: int):
    if not saved_route_service.delete_route(route_id): raise HTTPException(404, "Saved route not found")
