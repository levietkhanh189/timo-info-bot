# app/main.py

from fastapi import FastAPI
from app.api import endpoints
from app.core.config import settings
from app.core.logger import logger
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting up the Chatbot CV Portfolio application...")
    yield
    logger.info("Shutting down the Chatbot CV Portfolio application...")

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION,
    lifespan=lifespan
)

# Đăng ký các router
app.include_router(endpoints.router)
