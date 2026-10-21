from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio.session import AsyncSession

from app.config.database.app_database import app_session


# we will attempt to seed the roles here
async def role_seeder(session: Annotated[AsyncSession, Depends(app_session)]):
    pass
