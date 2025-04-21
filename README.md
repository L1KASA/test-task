# 🍽️ Restaurant Reservation System API

A FastAPI-based system for managing restaurant tables and reservations with PostgreSQL.

## 🌟 Main Components
app/
├── database.py # Database configuration and session management
├── dependencies.py # Dependency injection setup
├── exceptions.py # Custom exceptions
├── main.py # FastAPI application entry point
├── migrations/ # Alembic migration files
├── models/ # Database models
│ ├── base.py # Base model with common fields
│ ├── reservation.py # Reservation model
│ └── table.py # Table model
├── repositories/ # Data access layer
│ ├── abstract_base.py # Abstract base repository
│ ├── base.py # Base repository implementation
│ ├── reservation.py # Reservation repository
│ └── table.py # Table repository
├── routers/ # API endpoints
│ ├── reservation.py # Reservation API endpoints
│ └── table.py # Table API endpoints
├── schemas/ # Pydantic schemas
│ ├── base.py # Base Pydantic model
│ ├── reservation.py # Reservation schemas
│ └── table.py # Table schemas
└── services/ # Business logic
├── reservation.py # Reservation services
└── table.py # Table services
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
