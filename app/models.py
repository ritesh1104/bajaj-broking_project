from pydantic import BaseModel
from typing import Optional

class OrderRequest(BaseModel):
    symbol: str
    orderType: str 
    orderStyle: str  
    quantity: int
    price: Optional[float] = None
