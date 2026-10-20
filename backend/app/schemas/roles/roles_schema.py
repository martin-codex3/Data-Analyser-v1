from datetime import datetime

from pydantic import BaseModel, Field


class RoleSchema(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    description: str = Field(min_length=1, max_length=100)
    created_date: datetime = Field(default_factory=lambda: datetime.now())
    user_id: str | None
