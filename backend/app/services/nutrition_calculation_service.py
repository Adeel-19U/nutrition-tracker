from collections import defaultdict

from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from app.models.ingredient_nutrient import (
    IngredientNutrient
)

from app.models.nutrient import Nutrient

from app.schemas.calculation import (
    IngredientCalculationInput
)


def calculate_nutrition(
    db: Session,
    ingredients_input: list[
        IngredientCalculationInput
    ]
):

    ingredient_ids = [
        item.ingredient_id
        for item in ingredients_input
    ]

    ingredient_nutrients = (
        db.query(IngredientNutrient)
        .options(
            joinedload(
                IngredientNutrient.nutrient
            ),
            joinedload(
                IngredientNutrient.unit
            )
        )
        .filter(
            IngredientNutrient.ingredient_id.in_(
                ingredient_ids
            )
        )
        .all()
    )

    amount_lookup = {
        item.ingredient_id: item.amount_g
        for item in ingredients_input
    }

    totals = defaultdict(float)

    nutrient_metadata = {}

    for row in ingredient_nutrients:

        amount_g = amount_lookup.get(
            row.ingredient_id,
            0
        )

        nutrient_amount = (
            float(row.value_per_100g)
            * amount_g
        ) / 100

        nutrient_id = row.nutrient.id

        totals[nutrient_id] += nutrient_amount

        nutrient_metadata[nutrient_id] = {
            "name": row.nutrient.name,
            "slug": row.nutrient.slug,
            "unit": row.unit.symbol,
            "daily_recommended_value":
                row.nutrient.daily_recommended_value
        }

    response = []

    for nutrient_id, total_amount in totals.items():

        metadata = nutrient_metadata[
            nutrient_id
        ]

        daily_percent = None

        if metadata[
            "daily_recommended_value"
        ]:

            daily_percent = (
                total_amount
                / float(
                    metadata[
                        "daily_recommended_value"
                    ]
                )
            ) * 100

        response.append({
            "nutrient_id": nutrient_id,
            "nutrient_name":
                metadata["name"],
            "nutrient_slug":
                metadata["slug"],
            "amount":
                round(total_amount, 2),
            "unit":
                metadata["unit"],
            "daily_percent":
                round(daily_percent, 2)
                if daily_percent
                else None
        })

    response.sort(
        key=lambda x: x[
            "daily_percent"
        ]
        or 0,
        reverse=True
    )

    return response
