from fastapi import APIRouter
from app.database import trades

router = APIRouter(
    prefix="/api/v1/trades",
    tags=["Trades"]
)

@router.get("")
def get_trades():
    return trades
