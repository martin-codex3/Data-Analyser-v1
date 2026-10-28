import uuid
from datetime import UTC, datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.utils.base import Base

if TYPE_CHECKING:
    from app.models.roles.role_model import Role
    from app.models.tenant_users.tenant_user import TenantUsers


class MembershipRole(Base):
    __tablename__ = "membership_roles"
    tenant_user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("tenant_users.id"), primary_key=True
    )
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"), primary_key=True)
    created_date: Mapped[datetime] = mapped_column(default=lambda: datetime.now(UTC))

    # this will include the navigation tables here
    tenant_users: Mapped["Role"] = relationship(back_populates="roles")
    roles: Mapped["TenantUsers"] = relationship(back_populates="tenants")
