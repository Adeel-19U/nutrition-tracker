from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from app.models.ingredient import Ingredient
from app.models.ingredient_nutrient import (
    IngredientNutrient
)

from app.models.nutrient_tag_mapping import (
    NutrientTagMapping
)

from app.models.nutrient import Nutrient


def get_all_ingredients(
    db: Session
):

    ingredients = (
        db.query(Ingredient)
        .options(
            joinedload(
                Ingredient.nutrient_values
            )
            .joinedload(
                IngredientNutrient.nutrient
            )
            .joinedload(
                Nutrient.category
            ),

            joinedload(
                Ingredient.nutrient_values
            )
            .joinedload(
                IngredientNutrient.nutrient
            )
            .joinedload(
                Nutrient.group
            ),

            joinedload(
                Ingredient.nutrient_values
            )
            .joinedload(
                IngredientNutrient.nutrient
            )
            .joinedload(
                Nutrient.unit
            ),

            joinedload(
                Ingredient.nutrient_values
            )
            .joinedload(
                IngredientNutrient.unit
            ),

            joinedload(
                Ingredient.nutrient_values
            )
            .joinedload(
                IngredientNutrient.nutrient
            )
            .joinedload(
                Nutrient.aliases
            ),

            joinedload(
                Ingredient.nutrient_values
            )
            .joinedload(
                IngredientNutrient.nutrient
            )
            .joinedload(
                Nutrient.tag_mappings
            )
            .joinedload(
                NutrientTagMapping.tag
            )
        )
        .all()
    )

    return ingredients
