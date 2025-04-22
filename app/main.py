from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.routes import router as item_router

app = FastAPI(title=settings.APP_NAME)

app.include_router(item_router, prefix="/api/v1")
