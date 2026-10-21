from datetime import datetime
from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio.session import AsyncSession

from app.config.database.app_database import app_session

available_roles: list = [
    {
        "name": "owner",
        "description": "Full control over the organization. Can manage billing, delete the organization, manage members, and access all data and settings. There must be at least one owner per organization",
        "created_date": datetime.now(),
    },
    {
        "name": "admin",
        "description": "Can upload files, run analyses, use the AI assistant, and create reports. Cannot manage members or organization settings.",
        "created_date": datetime.now(),
    },
    {
        "name": "viewer",
        "description": "Read-only access. Can view datasets, dashboards, and reports shared with the organization, but cannot upload files, run analyses, or modify anything.",
        "created_date": datetime.now(),
    },
]


# we will attempt to seed the roles here
async def role_seeder(session: Annotated[AsyncSession, Depends(app_session)]):
    for role in available_roles:
        print(role)
