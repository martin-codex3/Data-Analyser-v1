from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.utils.base import Base

if TYPE_CHECKING:
    from app.models.tenants.tenant_model import Tenant


class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement="auto")
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(str(50), nullable=False)
    created_date: Mapped[datetime] = mapped_column(default_factory=lambda: datetime.now)
    tenant_id: Mapped[str] | None = mapped_column(ForeignKey("tenants.id"))
    tenant: Mapped["Tenant"] | None = relationship(back_populates="roles")
