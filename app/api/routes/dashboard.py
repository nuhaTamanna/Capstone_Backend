from fastapi import APIRouter
from app.schemas.dashboard import AuthorityDashboard
from app.services.dashboard_service import dashboard_service

router = APIRouter(prefix="/dashboard", tags=["dashboard"])


@router.get("/authority", response_model=AuthorityDashboard)
def authority_dashboard(): return dashboard_service.authority_dashboard()
