from typing import Annotated

from pydantic import BaseModel, EmailStr, Field, field_validator
from pydantic_extra_types.country import CountryAlpha3


class MalawiPhone:
    default_region_code = "MW"
    supported_regions = ["MW"]
    phone_format = "NATIONAL"


class TenantBaseSchema(BaseModel):
    first_name = Annotated[str, Field(min_length=2)]
    last_name: str = Field(min_length=3)
    phone_number: MalawiPhone
    address: str = Field(min_length=4)
    nationality: CountryAlpha3 = Field(min_length=1)
    email: EmailStr = Field(min_length=5)
    business_type: str = Field(min_length=2)
    password = Annotated[str, Field(pattern=r"[^&]")]
    profile_image: str | None = Field(max_length=50)

    @classmethod
    def profile_image_path(cls):
        if not cls.profile_image:
            cls.profile_image = "uploads/profile.jpg"
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
