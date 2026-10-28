from datetime import UTC, datetime
from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.utils.base import Base

if TYPE_CHECKING:
    from app.models.membership_roles.membership_role import MembershipRole


class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(50))
    created_date: Mapped[datetime] = mapped_column(default=lambda: datetime.now(UTC))
    tenant_users: Mapped[list["MembershipRole"]] = relationship(back_populates="roles")
