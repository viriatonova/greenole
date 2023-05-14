from fastapi import APIRouter
from measurement.routes import measurement_routes

router = APIRouter(
    prefix="/api/v1",
)


@router.get("/")
async def healthchecker() -> dict:
    return {"message": "Api is running"}


router.include_router(measurement_routes)
