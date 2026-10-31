import uuid
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


# for updating the application user
class UpdateApplicationUserSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)
    first_name: str | None = Field(default=None, min_length=5, max_length=40)
    last_name: str | None = Field(default=None, min_length=5, max_length=40)
    phone_number: MalawiPhone | None = Field(
        default=None,
    )
    email: EmailStr | None = Field(
        default=None,
    )
    username: str | None = Field(default=None, min_length=5, max_length=50)
    profile_image: str | None = Field(default=None, max_length=50)
    is_email_verified: bool | None = Field(default=False)
    account_verified_at: datetime = Field(default=datetime.now(UTC))
    password_hash: str | None = Field(default=None, min_length=5, max_length=20)

    @classmethod
    def profile_image_path(cls):
        if not cls.profile_image:
            return "assets/uploads/profile.jpg"

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


class ApplicationUserResponse(BaseModel):
    id: uuid.UUID
    first_name: str
    last_name: str
    phone_number: MalawiPhone
    email: EmailStr
    username: str
    profile_image: str
    is_email_verified: bool
    account_verified_at: datetime
