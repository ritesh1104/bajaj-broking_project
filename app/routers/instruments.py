from fastapi import APIRouter
from app.database import instruments

router = APIRouter(
    prefix="/api/v1/instruments",
    tags=["Instruments"]
)

@router.get("")
def get_instruments():
    return instruments
