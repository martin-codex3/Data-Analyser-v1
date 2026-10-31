from datetime import UTC, datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator
from pydantic_extra_types.phone_numbers import PhoneNumberValidator

MalawiPhone = Annotated[
    str, PhoneNumberValidator(default_region="MW", supported_regions=["MW"])
]


class ApplicationUserSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    first_name: str = Field(min_length=5, max_length=40)
    last_name: str = Field(min_length=5, max_length=40)
    phone_number: MalawiPhone
    email: EmailStr
    username: str | None = Field(min_length=5, max_length=50)
    profile_image: str | None = Field(max_length=50)
    is_email_verified: bool = Field(default=False)
    account_verified_at: datetime = Field(default=datetime.now(UTC))
    password_hash: str = Field(min_length=5, max_length=20)

    @field_validator("first_name")
    @classmethod
    def validate_first_name(cls, name: str) -> str:
        if not name.isalpha():
            raise ValueError("Your name should have letters only")
        return name.lower()

    @field_validator("last_name")
    @classmethod
    def validate_last_name(cls, name: str) -> str:
        if not name.isalpha():
            raise ValueError("Your name should have letters only")
        return name.lower()

    @field_validator("password_hash")
    @classmethod
    def validate_password(cls, value: str):
        if not value.istitle():
            raise ValueError("Password should have one uppercase")
        if len(value) <= 5:
            raise ValueError("Password should be more than 5 characters")

        return value
