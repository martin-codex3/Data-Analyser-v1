import uuid
from datetime import UTC, datetime
from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.tenant_users.tenant_user import TenantUsers
from app.utils.base import Base

if TYPE_CHECKING:
    from app.models.tenant_users.tenant_user import TenantUsers

DEFAULT_PROFILE_IMAGE = "media/profile_pics/default.jpg"


class ApplicationUser(Base):
    __tablename__ = "application_users"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, default=lambda: uuid.uuid4()
    )
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    phone_number: Mapped[str] = mapped_column(String(15))
    email: Mapped[str] = mapped_column(unique=True, index=True)
    username: Mapped[str | None] = mapped_column(String(100), nullable=True)
    profile_image: Mapped[str | None] = mapped_column(String(255), nullable=True)
    is_email_verified: Mapped[bool | None] = mapped_column(default=False, nullable=True)
    account_created_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(UTC)
    )
    bio: Mapped[str | None] = mapped_column(String(255), nullable=True)
    password_hash: Mapped[str] = mapped_column(String(255), index=True)
    tenants: Mapped[list["TenantUsers"]] = relationship(
        back_populates="users", lazy="selectin"
    )

    @property
    def set_default_profile_image(self):
        if not self.profile_image:
            return DEFAULT_PROFILE_IMAGE
        return f"/media/profile_pics/{self.profile_image}"
