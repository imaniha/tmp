"""
MongoDB connection and session management.
"""
from motor.motor_asyncio import AsyncIOMotorClient

from app.core.config import settings


class MongoDB:
    """MongoDB client singleton."""

    client: AsyncIOMotorClient | None = None
    database = None

    @classmethod
    async def connect(cls):
        """Connect to MongoDB."""
        if cls.client is None:
            try:
                cls.client = AsyncIOMotorClient(settings.DATABASE_URL)
                # Test the connection
                await cls.client.admin.command("ping")
                # Get database name from URL
                db_name = settings.DATABASE_URL.split("/")[-1].split("?")[0]
                cls.database = cls.client[db_name]
                print(f"Connected to MongoDB: {db_name}")
            else:
                # Test if still connected
                await cls.client.admin.command("ping")
        return cls.database

    @classmethod
    async def disconnect(cls):
        """Disconnect from MongoDB."""
        if cls.client:
            cls.client.close()
            cls.client = None
            cls.database = None
            print("Disconnected from MongoDB")

    @classmethod
    async def get_database(cls):
        """Get database instance."""
        if cls.database is None:
            await cls.connect()
        return cls.database


# Dependency to get database
async def get_database():
    """
    Get MongoDB database instance.

    Yields:
        Database instance
    """
    db = await MongoDB.get_database()
    try:
        yield db
    finally:
        pass  # Connection is managed by singleton

