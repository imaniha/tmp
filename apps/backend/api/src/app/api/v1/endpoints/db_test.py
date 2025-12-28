"""
Database test endpoint.
"""
from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.db.mongodb import get_database

router = APIRouter()


@router.get("/db-test")
async def test_database(db: AsyncIOMotorDatabase = Depends(get_database)):
    """
    Test database connection endpoint.

    Returns:
        Database connection status
    """
    try:
        # Test connection by listing collections
        collections = await db.list_collection_names()
        return {
            "status": "connected",
            "database": db.name,
            "collections": collections,
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
        }

