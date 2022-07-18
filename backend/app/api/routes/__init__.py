from fastapi import APIRouter
from api.routes.locations import router as locations_router


router = APIRouter()
router.include_router(locations_router, prefix="/locations", tags=["locations"])
