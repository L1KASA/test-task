# 🍽️ Restaurant Reservation System API

A FastAPI-based system for managing restaurant tables and reservations with PostgreSQL.

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
## 🚀 Quick Start

### Prerequisites
- Docker and Docker Compose
- Python 3.12 (for local development)

### With Docker (Recommended)
```bash docker-compose up --build ```

### Without Docker
#### 1. Install dependencies:
```bash pip install -r requirements.txt ```
### 2. Configure PostgreSQL in .env file:
```bash DATABASE_URL=postgresql://<user>:<password>@<host>:<port>/<dbname> ```
#### Apply migrations:
```bash alembic upgrade head ```
#### Start the development server:
```bash uvicorn app.main:app --reload ```
