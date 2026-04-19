from pydantic import BaseModel, Field
from typing import Dict, List


class PredictionResponse(BaseModel):

    predicted_category: str = Field(
        ...,
        description="Predicted insurance risk category",
        json_schema_extra={"example": "High"}
    )

    confidence: float = Field(
        ...,
        description="Model confidence score (0 to 1)",
        json_schema_extra={"example": 0.84}
    )

    class_probabilities: Dict[str, float] = Field(
        ...,
        description="Probability distribution across all risk categories",
        json_schema_extra={
            "example": {"Low": 0.01, "Medium": 0.15, "High": 0.84}
        }
    )

    base_premium: float = Field(
        ...,
        description="Initial calculated base premium before adjustments",
        json_schema_extra={"example": 1200}
    )

    city_multiplier: float = Field(
        ...,
        description="Risk adjustment based on city/location",
        json_schema_extra={"example": 1.3}
    )

    income_multiplier: float = Field(
        ...,
        description="Adjustment factor based on income level",
        json_schema_extra={"example": 0.9}
    )

    tax_factor: float = Field(
        ...,
        description="Regional insurance tax multiplier",
        json_schema_extra={"example": 1.15}
    )

    smoker_multiplier: float = Field(
        ...,
        description="Risk multiplier based on smoking status",
        json_schema_extra={"example": 1.4}
    )

    final_premium: float = Field(
        ...,
        description="Final calculated insurance premium after all adjustments",
        json_schema_extra={"example": 2050}
    )

    explanation: List[str] = Field(
        ...,
        description="Human-readable explanation of key risk factors"
    )

    savings_tips: List[str] = Field(
        ...,
        description="Personalized recommendations to reduce premium cost"
    )