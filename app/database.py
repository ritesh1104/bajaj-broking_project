from uuid import uuid4

USER_ID = "USER_001"

instruments = [
    {
        "symbol": "TCS",
        "exchange": "NSE",
        "instrumentType": "EQUITY",
        "lastTradedPrice": 3500
    },
    {
        "symbol": "INFY",
        "exchange": "NSE",
        "instrumentType": "EQUITY",
        "lastTradedPrice": 1450
    }
]

orders = {}
trades = []
portfolio = {}
