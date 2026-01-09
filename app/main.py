from fastapi import FastAPI
from app.routers import instruments, orders, trades, portfolio

app = FastAPI(
    title="Trading SDK – Bajaj Broking (Simulation)",
    description="Campus Hiring Assignment – Trading API Wrapper SDK",
    version="1.0.0"
)

app.include_router(instruments.router)
app.include_router(orders.router)
app.include_router(trades.router)
app.include_router(portfolio.router)
