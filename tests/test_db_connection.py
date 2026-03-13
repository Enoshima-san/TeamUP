```python
# Import necessary modules for testing and database operations
import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

# Import application settings
from src.teamup.core import settings

# Create an asynchronous database engine
engine = create_async_engine(
    settings.db.get_dsn(),  # Use the database DSN from application settings
    echo=settings.application.get_debug()  # Enable echo for debug mode
)

# Create an asynchronous session maker with the engine
async_session = async_sessionmaker(
    engine,  # Use the asynchronous database engine
    class_=AsyncSession,  # Use the asynchronous session class
    expire_on_commit=False  # Disable session expiration on commit
)


# Define a test function to verify database connection
@pytest.mark.asyncio
async def test_db_connection():
    """
    Test the database connection by executing a simple SQL query.

    :return: None
    """
    async with async_session() as session:  # Create an asynchronous session
        # Execute a SQL query to retrieve a single value
        res = await session.execute(text("SELECT 1"))
        # Assert that the query result is not None
        assert res.scalar() is not None
```