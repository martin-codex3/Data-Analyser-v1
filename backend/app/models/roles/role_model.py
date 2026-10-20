from datetime import UTC, datetime

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.tenant_roles.tenant_roles import tenant_roles
from app.models.tenants.tenant_model import Tenant
from app.utils.base import Base


class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(50))
    created_date: Mapped[datetime] = mapped_column(default=lambda: datetime.now(UTC))
    tenants: Mapped[list["Tenant"]] = relationship(
        secondary=tenant_roles, back_populates="roles"
    )
