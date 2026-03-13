```python
import asyncio

from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.sql import text

from ...core import logger, settings

# Create an asynchronous database engine with logging enabled in debug mode
engine = create_async_engine(
    settings.db.get_dsn(), echo=settings.application.get_debug()
)

# Create an asynchronous session maker with expire_on_commit set to False
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def check_database_connection(max_retries: int = 10, delay: int = 2) -> None:
    """
    Check if the database connection is available.

    Args:
    max_retries (int, optional): Maximum number of retries. Defaults to 10.
    delay (int, optional): Delay between retries in seconds. Defaults to 2.

    Raises:
    OperationalError: If the database connection is not available after max_retries attempts.
    """
    for attempt in range(1, max_retries + 1):
        try:
            # Establish an asynchronous database session
            async with async_session() as session:
                # Execute a simple query to check the connection
                await session.execute(text("SELECT 1"))
            logger.info(f"Database connection established on attempt {attempt}")
            return
        except OperationalError as e:
            if attempt == max_retries:
                # Raise the exception if all retries fail
                raise e
            logger.warning(
                f"Database not ready ({attempt}/{max_retries} attempts), retrying in {delay} seconds..."
            )
            # Wait for the specified delay before retrying
            await asyncio.sleep(delay)
```