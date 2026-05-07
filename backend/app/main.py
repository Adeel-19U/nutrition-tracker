from fastapi import FastAPI

from app.routes.ingredients import router as ingredients_router
from app.routes.nutrients import router as nutrients_router
from app.routes.calculations import router as calculations_router


from app.models.ingredient import Ingredient
from app.models.unit import Unit
from app.models.nutrient import Nutrient
from app.models.ingredient_nutrient import IngredientNutrient
from app.models.nutrient import Nutrient
from app.models.nutrient_category import NutrientCategory
from app.models.nutrient_group import NutrientGroup
from app.models.nutrient_alias import NutrientAlias
from app.models.nutrient_tag import NutrientTag
from app.models.nutrient_tag_mapping import NutrientTagMapping
from app.models.unit import Unit
from app.models.nutrient_relationship import NutrientRelationship


app = FastAPI()

app.include_router(
    ingredients_router,
    prefix="/ingredients",
    tags=["Ingredients"]
)

app.include_router(
    nutrients_router,
    prefix="/nutrients",
    tags=["Nutrients"]
)

app.include_router(
    calculations_router,
    prefix="/calculations",
    tags=["Calculations"]
)

@app.get("/")
def root():
    return {
        "message": "Nutrition Tracker API running"
    }
