from fastapi import APIRouter
from sensor.routes import sensor_routes


router = APIRouter(
    prefix="/api/v1",
)

@router.get("/")
async def healthchecker() -> dict:
    return {"message": "API is running "}


router.include_router(sensor_routes)
