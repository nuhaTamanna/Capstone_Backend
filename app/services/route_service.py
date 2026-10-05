from app.schemas.route import SavedRoute, SavedRouteCreate


class SavedRouteService:
    def __init__(self) -> None:
        self._routes = [SavedRoute(id=1, name="Home to Campus", origin="Rajagiriya", destination="University of Colombo")]
        self._next_id = 2
    def list_routes(self) -> list[SavedRoute]: return self._routes
    def create_route(self, payload: SavedRouteCreate) -> SavedRoute:
        route = SavedRoute(id=self._next_id, **payload.model_dump()); self._routes.append(route); self._next_id += 1; return route
    def delete_route(self, route_id: int) -> bool:
        before = len(self._routes); self._routes = [r for r in self._routes if r.id != route_id]; return len(self._routes) != before


saved_route_service = SavedRouteService()
