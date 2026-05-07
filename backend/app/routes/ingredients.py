from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.ingredient import (
    IngredientResponse
)

from app.services.ingredient_service import (
    get_all_ingredients
)


router = APIRouter()


@router.get(
    "/",
    response_model=list[IngredientResponse]
)
def ingredients(
    db: Session = Depends(get_db)
):

    return get_all_ingredients(db)
