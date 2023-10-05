from fastapi import APIRouter

from app.api.endpoints.charity_projects import router as charity_router
from app.api.endpoints.donations import router as donation_router

main_router = APIRouter()

main_router.include_router(charity_router)
main_router.include_router(donation_router)
