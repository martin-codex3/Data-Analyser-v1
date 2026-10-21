from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio.session import AsyncSession

from app.config.database.app_database import app_session
from app.models.roles.role_model import Role

roles_router = APIRouter()


# we will get all the routes
@roles_router.get("/")
async def get_roles(session: Annotated[AsyncSession, Depends(app_session)]):
    """This will fetch all the available roles"""
    statement = await session.execute(select(Role))
    results = statement.scalars().all()
    return results
