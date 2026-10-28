from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio.session import AsyncSession

from app.config.database.app_database import app_session
from app.models.roles.role_model import Role
from app.schemas.tenants.tenant_schemas import CreateTenantSchema

tenant_routes = APIRouter()


@tenant_routes.post(
    "/create-account",
)
async def create_tenant_account(
    tenant_data: CreateTenantSchema,
    session: Annotated[AsyncSession, Depends(app_session)],
):
    async with session.begin():
        statement = await session.execute(
            select(Role).where(
                func(Role.name) == "admin",
            )
        )
