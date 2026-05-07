from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.nutrient import NutrientResponse

from app.services.nutrient_service import (
    get_all_nutrients
)

from app.services.nutrient_tree_service import (
    get_nutrient_tree
)

router = APIRouter()


@router.get(
    "/",
    response_model=list[NutrientResponse]
)
def get_nutrients(
    db: Session = Depends(get_db)
):

    return get_all_nutrients(db)

@router.get("/tree/{slug}")
def nutrient_tree(
    slug: str,
    db: Session = Depends(get_db)
):

    return get_nutrient_tree(
        db,
        slug
    )
