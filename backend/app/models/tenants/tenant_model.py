import uuid
from datetime import UTC, datetime
from typing import TYPE_CHECKING

from sqlalchemy import JSON, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.utils.base import Base

if TYPE_CHECKING:
    from app.models.tenant_users.tenant_user import TenantUsers


class Tenant(Base):
    __tablename__ = "tenants"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, default=lambda: uuid.uuid4()
    )
    business_name: Mapped[str] = mapped_column(String(255))
    business_type: Mapped[str] = mapped_column(String(100))
    business_email: Mapped[str] = mapped_column(String(200))
    business_phone: Mapped[str] = mapped_column(String(30))
    registration_number: Mapped[str | None] = mapped_column(String(50), nullable=True)
    industry: Mapped[str | None] = mapped_column(String(255), nullable=True)
    address_line_1: Mapped[str | None] = mapped_column(String(30), nullable=True)
    address_line_2: Mapped[str | None] = mapped_column(String(50), nullable=True)
    city: Mapped[str | None] = mapped_column(String(40), nullable=True)
    region: Mapped[str | None] = mapped_column(String(50), nullable=True, index=True)
    postal_code: Mapped[str | None] = mapped_column(
        String(100), nullable=True, index=True
    )
    country_code: Mapped[str | None] = mapped_column(
        String(40), nullable=True, index=True
    )
    status: Mapped[str | None] = mapped_column(String(30), nullable=True)
    website_url: Mapped[str | None] = mapped_column(String(100), nullable=True)
    slug: Mapped[str | None] = mapped_column(String(255), unique=True, nullable=True)
    settings: Mapped[dict] = mapped_column(JSON, nullable=True, default=dict)
    created_by_id: Mapped[uuid.UUID | None] = mapped_column(
        default=lambda: uuid.uuid4(), index=True, nullable=True
    )
    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(UTC))
    updated_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(UTC))
    buiness_logo: Mapped[str | None] = mapped_column(String(100), nullable=True)
    description: Mapped[str | None] = mapped_column(
        String(255), nullable=True, index=True
    )
    users: Mapped[list["TenantUsers"]] = relationship(
        back_populates="tenants", lazy="selectin"
    )
