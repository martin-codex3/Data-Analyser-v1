from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi_faults import FaultRegistry

from app.config.database.app_database import app_database_engine, app_database_init
from app.routes.roles.roles_router import roles_router
from app.routes.tenants.tenant_routes import tenant_routes

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

# we will mount the static files here
app.mount("/static/uploads", StaticFiles(directory="static/uploads"), name="static")

# for the app faults configurations
faults = FaultRegistry(faults=[], name="Api Faults")


app.include_router(router=roles_router, prefix="/api/roles", tags=["Roles"])
app.include_router(router=tenant_routes, prefix="/api/tenants", tags=["Tenants"])

# we will configure the cors here
origins = ["http://localhost:5173", "http://localhost:8080"]

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=origins,
    allow_headers=["*"],
    allow_methods=["*"],
)

api_faults = FaultRegistry.merge(
    faults, name="api", type_base="https://api.example.com/problems"
)

api_faults.install(
    app=app,
    include_http_exceptions=True,
    include_unhandled_error=True,
    include_validation_error=True,
)
