import uuid

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.tenant_users.tenant_user import tenant_users
from app.models.tenants.tenant_model import Tenant
from app.utils.base import Base


class ApplicationUser(Base):
    __tablename__ = "application_users"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    phone_number: Mapped[str] = mapped_column(String(15))
    email: Mapped[str] = mapped_column(unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(20), index=True)
    tenants: Mapped[list["Tenant"]] = relationship(
        back_populates="application_users", lazy="selectin", secondary=tenant_users
    )
