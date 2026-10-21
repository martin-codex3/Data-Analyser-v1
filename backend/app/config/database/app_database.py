from sqlalchemy.ext.asyncio.engine import create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession, async_sessionmaker

from app.config.settings.app_settings import AppSettings
from app.models.roles.role_model import Role  # noqa: F401
from app.models.tenants.tenant_model import Tenant  # noqa: F401
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


Session = async_sessionmaker(
    bind=app_database_engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=True,
)


async def app_session():
    """This will establish the app database session.
    It will be used as a dependency"""
    async with Session() as session:
        yield session
