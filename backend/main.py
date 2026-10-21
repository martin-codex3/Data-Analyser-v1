from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi_faults import FaultRegistry

from app.config.database.app_database import app_database_engine, app_database_init
from app.routes.roles.roles_router import roles_router

api_version: str = "v1"


# app lifespan
@asynccontextmanager
async def app_life_span(app: FastAPI):
    await app_database_init()
    yield
    await app_database_engine.dispose()


app = FastAPI(
    version=api_version,
    title="Document Analyser",
    description="Modern document analyser using fastapi and sveltekit",
    lifespan=app_life_span,
)

# for the app faults configurations
faults = FaultRegistry(faults=[], name="Api Faults")


app.include_router(router=roles_router, prefix="/api/roles", tags=["Roles"])

api_faults = FaultRegistry.merge(
    faults, name="api", type_base="https://api.example.com/problems"
)

api_faults.install(
    app=app,
    include_http_exceptions=True,
    include_unhandled_error=True,
    include_validation_error=True,
)
