import uuid
from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.tenant_users.tenant_user import TenantUsers
from app.utils.base import Base

if TYPE_CHECKING:
    from app.models.tenant_users.tenant_user import TenantUsers


class ApplicationUser(Base):
    __tablename__ = "application_users"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, default=lambda: uuid.uuid4()
    )
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    phone_number: Mapped[str] = mapped_column(String(15))
    email: Mapped[str] = mapped_column(unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(20), index=True)
    tenants: Mapped[list["TenantUsers"]] = relationship(
        back_populates="users", lazy="selectin"
    )
