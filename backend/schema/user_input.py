from pydantic import BaseModel, Field, field_validator
from typing import Literal


class UserInput(BaseModel):
    
    

    age: int = Field(
        ...,
        ge=18,
        le=65,
        description="Age (18–65 years)"
    )

    weight: float = Field(
        ...,
        ge=55,
        le=100,
        description="Weight in kg (55–100)"
    )

    height: float = Field(
        ...,
        ge=160,
        le=195,
        description="Height in cm (160–195)"
    )

    income_dkk: float = Field(
        ...,
        ge=280000,
        le=800000,
        description="Annual income in DKK (280k–800k)"
    )

    smoker: bool = Field(..., description="Whether user is a smoker")

    city: str = Field(..., description="City of residence")

    country: str = Field("Denmark", description="Country (default Denmark 🇩🇰)")

    occupation: Literal[
        'retired','freelancer','student','government_job',
        'business_owner','unemployed','private_job'
    ] = Field(..., description="Occupation type")

    @field_validator("city")
    @classmethod
    def normalize_city(cls, v):
        if v is None or str(v).strip() == "":
           return "Unknown"
        return str(v).strip().title()