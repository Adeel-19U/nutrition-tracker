from pydantic import BaseModel
from uuid import UUID

from app.schemas.nutrient import (
    NutrientResponse,
    UnitResponse
)


class IngredientNutrientResponse(BaseModel):

    id: UUID

    value_per_100g: float

    nutrient: NutrientResponse

    unit: UnitResponse

    class Config:
        from_attributes = True


class IngredientResponse(BaseModel):

    id: UUID

    name: str

    nutrient_values: list[
        IngredientNutrientResponse
    ]

    class Config:
        from_attributes = True
