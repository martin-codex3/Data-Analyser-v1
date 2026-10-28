import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.utils.base import Base

if TYPE_CHECKING:
    from app.models.roles.role_model import Role
    from app.models.tenant_users.tenant_user import TenantUsers


class TenantMembership(Base):
    __tablename__ = "tenant_memberships"

    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"), primary_key=True)
    tenant_user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("tenant_users.id"), primary_key=True
    )

    roles: Mapped["Role"] = relationship(back_populates="tenant_users")
    tenant_users: Mapped["TenantUsers"] = relationship(back_populates="roles")
