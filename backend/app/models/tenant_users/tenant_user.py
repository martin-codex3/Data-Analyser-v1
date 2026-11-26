import uuid
from datetime import UTC, datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.documents.document_model import Document
from app.utils.base import Base

if TYPE_CHECKING:
    from app.models.application_users.application_user import ApplicationUser
    from app.models.tenants.tenant_model import Tenant


class TenantUsers(Base):
    __tablename__ = "tenant_users"
    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, default=lambda: uuid.uuid4()
    )
    tenant_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("tenants.id"))
    application_user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("application_users.id")
    )

    # extra data
    role: Mapped[str] = mapped_column(String(50))
    created_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(UTC)
    )
    updated_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(UTC)
    )

    # this will also include the parents and the childrens of both tables
    tenants: Mapped["Tenant"] = relationship(back_populates="users", lazy="selectin")
    users: Mapped["ApplicationUser"] = relationship(
        back_populates="tenants", lazy="selectin"
    )
    documents: Mapped[list[Document]] = relationship(
        back_populates="tenant_user", lazy="selectin"
    )
