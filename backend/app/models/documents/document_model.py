import uuid
from datetime import UTC, datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.utils.base import Base

if TYPE_CHECKING:
    from app.models.tenant_users.tenant_user import TenantUsers


class Document(Base):
    __tablename__ = "documents"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, default=lambda: uuid.uuid4()
    )

    file_name: Mapped[str] = mapped_column(String(255), index=True)
    file_size: Mapped[str] = mapped_column(String(255))
    document_type: Mapped[str] = mapped_column(String(255))
    document_version: Mapped[str] = mapped_column(String(255))
    document_status: Mapped[str] = mapped_column(String(100))
    document_page_count: Mapped[str] = mapped_column(String(100))
    document_description: Mapped[str] = mapped_column(String(255), index=True)
    processed_by: Mapped[str] = mapped_column(String(100))
    processed_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(UTC)
    )
    created_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(UTC)
    )
    updated_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(UTC)
    )

    tenant_user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("tenant_users.id"))
    tenat_user = Mapped[TenantUsers] = relationship(
        back_populates="documents", lazy="selectin"
    )
