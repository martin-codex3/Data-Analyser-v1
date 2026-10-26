import uuid
from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.tenant_roles.tenant_roles import tenant_roles
from app.utils.base import Base

if TYPE_CHECKING:
    from app.models.roles.role_model import Role
    from app.models.tenant_users.tenant_user import TenantUsers


class Tenant(Base):
    __tablename__ = "tenants"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, default=lambda: uuid.uuid4()
    )
    business_name: Mapped[str] = mapped_column(String(255))
    business_type: Mapped[str] = mapped_column(String(100))
    address: Mapped[str] = mapped_column(String(100))
    nationality: Mapped[str] = mapped_column(index=True)
    users: Mapped[list["TenantUsers"]] = relationship(back_populates="tenants")
    roles: Mapped[list["Role"]] = relationship(
        secondary=tenant_roles, back_populates="roles"
    )
