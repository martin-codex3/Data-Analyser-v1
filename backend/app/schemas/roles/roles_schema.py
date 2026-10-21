import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class RoleSchemaBase(BaseModel):
    name: str = Field(min_length=1)
    description: str = Field(min_length=1)
    created_date: datetime = Field(default_factory=lambda: datetime.now())


# for add new roles
class CreateRoleSchema(BaseModel):
    name: str = Field(min_length=1)
    description: str = Field(min_length=10)


# for assigning roles to user
class AssignRoleToUser(BaseModel):
    role_id: int
    tenant_id: uuid.UUID


# for updating the roles
class UpdateRoleSchema(BaseModel):
    name: str | None = Field(default=None, min_length=1)
    description: str | None = Field(default=None, min_length=1)
    model_config = ConfigDict(extra="ignore")


# for the role response
class RoleReponseSchema(RoleSchemaBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
