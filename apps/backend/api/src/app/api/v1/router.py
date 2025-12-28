"""
API v1 router.
"""
from fastapi import APIRouter

from app.api.v1.endpoints import health, db_test

api_router = APIRouter()

# Include endpoint routers
api_router.include_router(health.router, tags=["health"])
api_router.include_router(db_test.router, tags=["database"])

