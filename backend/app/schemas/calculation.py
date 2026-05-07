from pydantic import BaseModel
from uuid import UUID


class IngredientCalculationInput(
    BaseModel
):
    ingredient_id: UUID
    amount_g: float


class NutrientTotalResponse(
    BaseModel
):
    nutrient_id: UUID

    nutrient_name: str

    nutrient_slug: str

    amount: float

    unit: str

    daily_percent: float | None


class NutritionCalculationResponse(
    BaseModel
):
    totals: list[
        NutrientTotalResponse
    ]
