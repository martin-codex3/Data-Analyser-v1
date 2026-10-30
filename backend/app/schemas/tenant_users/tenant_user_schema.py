from pydantic import BaseModel, ConfigDict

from app.schemas.application_users.application_user_schemas import ApplicationUserSchema
from app.schemas.tenants.tenant_schemas import CreateTenantSchema


class CreateTenantUserSchema(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    application_user_schema: ApplicationUserSchema
    tenant_schema: CreateTenantSchema
