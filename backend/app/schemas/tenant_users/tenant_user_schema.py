from typing import Annotated

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator
from pydantic_extra_types.phone_numbers import PhoneNumberValidator

MalawiPhone = Annotated[
    str, PhoneNumberValidator(default_region="MW", supported_regions=["MW"])
]


class CreateTenantUserSchema(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    first_name: str = Field(min_length=5, max_length=40)
    last_name: str = Field(min_length=5, max_length=40)
    phone_number: MalawiPhone
    email: EmailStr
    business_name: str = Field(min_length=5, max_length=40)
    business_type: str = Field(min_length=2)
    business_email: EmailStr
    business_phone: MalawiPhone
    address_line_1: str = Field(min_length=5, max_length=100)
    password_hash: str = Field(min_length=10, max_length=20)

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
        if len(value) <= 10:
            raise ValueError("Password should be more than 10 characters")
        if len(value) > 20:
            raise ValueError("Password must not be more than 20 characters")

        return value
