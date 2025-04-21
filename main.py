from fastapi import FastAPI
from app.routers import table
from app.database import engine, Base
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

Base.metadata.create_all(bind=engine)

app = FastAPI()
from app.routers.table import router as tables_router
from app.routers.reservation import router as reservations_router
app.include_router(tables_router)
app.include_router(reservations_router)

@app.get("/")
def read_root():
    return {"message": "Welcome"}
