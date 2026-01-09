from fastapi import APIRouter
from app.database import portfolio

router = APIRouter(
    prefix="/api/v1/portfolio",
    tags=["Portfolio"]
)

@router.get("")
def get_portfolio():
    return list(portfolio.values())
