from fastapi import APIRouter, HTTPException
from uuid import uuid4
from app.models import OrderRequest
from app.database import orders, trades, portfolio

router = APIRouter(
    prefix="/api/v1/orders",
    tags=["Orders"]
)

@router.post("")
def place_order(order: OrderRequest):

    if order.quantity <= 0:
        raise HTTPException(status_code=400, detail="Quantity must be greater than 0")

    if order.orderStyle == "LIMIT" and order.price is None:
        raise HTTPException(status_code=400, detail="Price is required for LIMIT order")

    order_id = str(uuid4())

    order_status = "EXECUTED" if order.orderStyle == "MARKET" else "PLACED"

    orders[order_id] = {
        "orderId": order_id,
        "symbol": order.symbol,
        "orderType": order.orderType,
        "orderStyle": order.orderStyle,
        "quantity": order.quantity,
        "price": order.price,
        "status": order_status
    }

    if order.orderStyle == "MARKET":
        trade = {
            "tradeId": str(uuid4()),
            "orderId": order_id,
            "symbol": order.symbol,
            "quantity": order.quantity,
            "price": order.price or 0
        }
        trades.append(trade)

        existing_qty = portfolio.get(order.symbol, {}).get("quantity", 0)

        portfolio[order.symbol] = {
            "symbol": order.symbol,
            "quantity": existing_qty + order.quantity,
            "averagePrice": order.price or 0,
            "currentValue": (existing_qty + order.quantity) * (order.price or 0)
        }

    return orders[order_id]


@router.get("/{order_id}")
def get_order_status(order_id: str):
    if order_id not in orders:
        raise HTTPException(status_code=404, detail="Order not found")
    return orders[order_id]
