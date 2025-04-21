# 🍽️ Restaurant Reservation System API

A FastAPI-based system for managing restaurant tables and reservations with PostgreSQL.

## 🌟 Main Components
```text
app/
├── database.py          # Конфигурация базы данных
├── dependencies.py      # Инъекция зависимостей
├── exceptions.py        # Кастомные исключения
├── main.py              # Точка входа FastAPI
├── migrations/          # Миграции Alembic
├── models/              # Модели базы данных
│   ├── base.py          # Базовая модель
│   ├── reservation.py   # Модель бронирования
│   └── table.py         # Модель столика
├── repositories/        # Доступ к данным
│   ├── abstract_base.py # Абстрактный репозиторий
│   ├── base.py          # Базовый репозиторий
│   ├── reservation.py   # Репозиторий бронирований
│   └── table.py         # Репозиторий столиков
├── routers/             # API endpoints
│   ├── reservation.py   # Роуты бронирований
│   └── table.py         # Роуты столиков
├── schemas/             # Pydantic схемы
│   ├── base.py          # Базовая схема
│   ├── reservation.py   # Схемы бронирований
│   └── table.py         # Схемы столиков
└── services/            # Бизнес-логика
    ├── reservation.py   # Сервис бронирований
    └── table.py         # Сервис столиков
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
