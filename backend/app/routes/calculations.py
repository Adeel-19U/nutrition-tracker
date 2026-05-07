from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.calculation import (
    IngredientCalculationInput,
    NutritionCalculationResponse
)

from app.services.nutrition_calculation_service import (
    calculate_nutrition
)


router = APIRouter()


@router.post(
    "/nutrition",
    response_model=
        NutritionCalculationResponse
)
def nutrition_calculation(
    ingredients:
        list[
            IngredientCalculationInput
        ],

    db: Session = Depends(get_db)
):

    totals = calculate_nutrition(
        db,
        ingredients
    )

    return {
        "totals": totals
    }
