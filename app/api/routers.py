from fastapi import APIRouter

from app.api.endpoints.charity_project import router as charity_router
from app.api.endpoints.donation import router as donation_router
from app.api.endpoints.users import router as user_router

main_router = APIRouter()

main_router.include_router(charity_router)
main_router.include_router(donation_router)
main_router.include_router(user_router)
