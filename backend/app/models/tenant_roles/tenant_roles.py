from sqlalchemy import Column, ForeignKey, Table

from app.utils.base import Base

tenant_roles = Table(
    "tenant_roles",
    Base.metadata,
    Column("tenant_id", ForeignKey("tenants.id")),
    Column("role_id", ForeignKey("roles.id")),
)
