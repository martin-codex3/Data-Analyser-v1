import uuid
from datetime import UTC, datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.utils.base import Base

if TYPE_CHECKING:
    from app.models.application_users.application_user import ApplicationUser
    from app.models.tenant_memberships.tenant_membership import TenantMembership
    from app.models.tenants.tenant_model import Tenant


class TenantUsers(Base):
    __tablename__ = "tenant_users"

    tenant_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("tenants.id"), primary_key=True
    )
    application_user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("application_users.id"), primary_key=True
    )

    # extra data
    created_date: Mapped[datetime] = mapped_column(default=datetime.now(UTC))
    updated_date: Mapped[datetime] = mapped_column(default=datetime.now(UTC))

    # this will also include the parents and the childrens of both tables
    tenants: Mapped["Tenant"] = relationship(back_populates="users", lazy="selectin")
    users: Mapped["ApplicationUser"] = relationship(
        back_populates="tenants", lazy="selectin"
    )
    roles: Mapped[list["TenantMembership"]] = relationship(
        back_populates="tenant_users"
    )
