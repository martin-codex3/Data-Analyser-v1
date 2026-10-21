import asyncio
from datetime import datetime

import typer
from sqlalchemy import select

from app.config.database.app_database import (
    Session,
    app_database_engine,
    app_database_init,
)
from app.models.roles.role_model import Role

app = typer.Typer()

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


async def _seed_roles():
    await app_database_init()
    async with Session() as session:
        existing_roles = await session.execute(select(Role.name))

        results = existing_roles.scalars().all()
        for role in available_roles:
            if role["name"] not in results:
                new_roles = Role(**role)
                session.add(new_roles)
                await session.commit()
        await app_database_engine.dispose()


@app.command()
def seed_roles():
    asyncio.run(_seed_roles())


if __name__ == "__main__":
    app()
