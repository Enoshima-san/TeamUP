```python
import asyncio

from src.teamup.core import logger
from src.teamup.infra import Base, engine


async def create_database():
    """
    Creates all database tables using Alembic's metadata.

    This function is designed to be run asynchronously, allowing for concurrent execution
    of other tasks while the database is being created.
    """
    async with engine.begin() as conn:
        # Run the create_all operation on the database connection
        await conn.run_sync(Base.metadata.create_all)
    # Log a success message to the console
    logger.info("All tables created successfully!")


def run_create_all():
    """
    Runs the create_database function using asyncio.

    This function is the entry point for creating the database tables.
    """
    asyncio.run(create_database())


if __name__ == "__main__":
    # Run the create_all operation when the script is executed directly
    run_create_all()
```