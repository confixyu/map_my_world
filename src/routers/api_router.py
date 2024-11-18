from fastapi import APIRouter

from src.routers.locations import location_router
from src.routers.categories import category_router
from src.routers.location_category import location_category_router


api_router = APIRouter()
api_router.include_router(location_router)
api_router.include_router(category_router)
api_router.include_router(location_category_router)
