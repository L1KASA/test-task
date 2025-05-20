# 🍽️ Restaurant Reservation System API

A FastAPI-based system for managing restaurant tables and reservations with PostgreSQL.
![Image alt](https://raw.githubusercontent.com/L1KASA/test-task/4c594533569677bd125c22b991f0de3d0f3a49cd/last.jpg)
## 🌟 Main Components
```text
app/
├── database.py          # Database configuration
├── dependencies.py     # Dependency injection
├── exceptions.py       # Custom exceptions
├── main.py             # FastAPI entry point
├── migrations/         # Alembic migrations
├── models/             # Database models
│   ├── base.py         # Base model
│   ├── reservation.py  # Reservation model
│   └── table.py        # Table model
├── repositories/       # Data access layer
│   ├── abstract_base.py # Abstract repository
│   ├── base.py         # Base repository
│   ├── reservation.py  # Reservation repository
│   └── table.py        # Table repository
├── routers/            # API endpoints
│   ├── reservation.py  # Reservation routes
│   └── table.py        # Table routes
├── schemas/            # Pydantic schemas
│   ├── base.py         # Base schema
│   ├── reservation.py  # Reservation schemas
│   └── table.py        # Table schemas
└── services/           # Business logic
    ├── reservation.py  # Reservation services
    └── table.py        # Table services
```
## 🚀 Quick Start (Windows)

### Prerequisites
- Docker and Docker Compose
- Python 3.12 (for local development)

### With Docker (Recommended)
```docker-compose up --build```

### Without Docker
#### 1. Install dependencies:
```python -m pip install -r requirements.txt```
#### 2. Configure PostgreSQL in .env file:
```DATABASE_URL=postgresql://<user>:<password>@<host>:<port>/<dbname>```
#### 3. Apply migrations:
```alembic upgrade head```
#### 4. Start the development server:
```uvicorn app.main:app --reload```
