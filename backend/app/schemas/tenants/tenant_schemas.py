from typing import Annotated

import phonenumbers
from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator
from pydantic_extra_types.country import CountryAlpha3
from pydantic_extra_types.phone_numbers import PhoneNumberValidator


class TenantBaseSchema(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    first_name: str = Field(min_length=3, max_length=30)
    last_name: str = Field(min_length=3, max_length=30)
    phone_number = Annotated[
        str | phonenumbers.PhoneNumber, PhoneNumberValidator(number_format="E164")
    ]
    address: str = Field(min_length=3, max_length=30)
    nationality: CountryAlpha3 = Field(min_length=1)
    email: EmailStr = Field(min_length=5)
    business_type: str = Field(min_length=2)
    password: str = Field(min_length=5, max_length=30)
    profile_image: str | None = Field(max_length=50)

    @classmethod
    def profile_image_path(cls):
        if not cls.profile_image:
            cls.profile_image = "uploads/profile.jpg"
        else:
            return cls.profile_image


# for creating a new tenant
class CreateTenantSchema(BaseModel):
    first_name: str = Field(min_length=3, max_length=30)
    last_name: str = Field(min_length=3, max_length=30)
    phone_number = Annotated[
        str | phonenumbers.PhoneNumber, PhoneNumberValidator(number_format="E164")
    ]
    address: str = Field(min_length=4)
    nationality: CountryAlpha3 = Field(min_length=1)
    email: EmailStr = Field(min_length=5)
    business_type: str = Field(min_length=2)
    password: str = Field(min_length=5, max_length=30)

    model_config = ConfigDict(arbitrary_types_allowed=True)

    @classmethod
    def profile_image_path(cls):
        if not cls.profile_image:
            cls.profile_image = "static/uploads/profile.jpg"
        else:
            return cls.profile_image

    @field_validator("first_name")
    @classmethod
    def validate_first_name(cls, name: str) -> str:
        if not name.isalpha() or name.isnumeric():
            raise ValueError("Your name should have letters only")
        return name.lower()

    @field_validator("last_name")
    @classmethod
    def validate_last_name(cls, name: str) -> str:
        if not name.isalpha() or name.isnumeric():
            raise ValueError("Your name should have letters only")
        return name.lower()
