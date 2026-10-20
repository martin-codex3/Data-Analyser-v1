from sqlalchemy.ext.asyncio.engine import create_async_engine

from app.config.settings.app_settings import AppSettings
from app.utils.base import Base

# we will create the database engine here
app_database_engine = create_async_engine(
    url=AppSettings.public_database_url, echo=True
)


# we will now initialise the database connection
async def app_database_init():
    """this will establish the database connection
    and all the associated tables will be created automatically"""
    async with app_database_engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
