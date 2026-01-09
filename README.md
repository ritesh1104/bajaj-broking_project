# Trading SDK – Bajaj Broking

## 📌 Overview
This project is a **simulated Trading Backend SDK** developed as part of a **Campus Hiring Assignment**.  
It mimics the core functionalities of an online stock broking platform such as Bajaj Broking.

The system is **not connected to real markets** and is intended only for **design, structure, and concept demonstration**.

---

## 🎯 Features Implemented
- View available financial instruments
- Place BUY / SELL orders
- Support for MARKET and LIMIT orders
- Fetch order status
- View executed trades
- View portfolio holdings
- Basic order execution simulation
- In-memory data storage
- Swagger / OpenAPI documentation

---

## 🛠 Technology Stack
- **Language:** Python 3.10
- **Framework:** FastAPI
- **API Format:** REST (JSON)
- **Storage:** In-memory (Python dict & list)
- **Documentation:** Swagger UI (auto-generated)

---


---

## ⚙️ Setup & Run Instructions (Anaconda)

### 1️. Create virtual environment
```bash
conda create -n trading-sdk python=3.10
```

### 2. Activate environment
```bash
conda activate trading-sdk
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the server
```bash
uvicorn app.main:app --reload
```




