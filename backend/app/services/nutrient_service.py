from sqlalchemy.orm import joinedload
from sqlalchemy.orm import Session

from app.models.nutrient import Nutrient
from app.models.nutrient_tag_mapping import NutrientTagMapping


def get_all_nutrients(
    db: Session
):

    nutrients = (
        db.query(Nutrient)
        .options(
            joinedload(Nutrient.category),
            joinedload(Nutrient.group),
            joinedload(Nutrient.unit),
            joinedload(Nutrient.aliases),
            joinedload(Nutrient.tag_mappings)
                .joinedload(NutrientTagMapping.tag)
        )
        .order_by(Nutrient.display_order)
        .all()
    )

    return nutrients
