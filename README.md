# Trading SDK – Bajaj Broking

## Overview
This project is a simulated Trading API backend built as part of a campus hiring assignment.
It demonstrates core trading workflows such as:
- Viewing instruments
- Placing buy/sell orders
- Checking order status
- Viewing executed trades
- Fetching portfolio holdings

No real market connectivity is used.

---

## Tech Stack
- Python
- FastAPI
- In-memory storage
- Swagger/OpenAPI

---

## Setup Instructions (Anaconda)

```bash
conda create -n trading-sdk python=3.10
conda activate trading-sdk
pip install -r requirements.txt
uvicorn app.main:app --reload
