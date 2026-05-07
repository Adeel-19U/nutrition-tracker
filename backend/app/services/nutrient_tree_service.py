from sqlalchemy.orm import Session

from app.models.nutrient import Nutrient
from app.models.nutrient_relationship import (
    NutrientRelationship
)


def build_nutrient_tree(
    nutrient_id,
    relationships_map,
    nutrient_map
):

    nutrient = nutrient_map.get(nutrient_id)

    if not nutrient:
        return None

    children_relationships = relationships_map.get(
        nutrient_id,
        []
    )

    children = []

    for relationship in children_relationships:

        child_tree = build_nutrient_tree(
            relationship.child_nutrient_id,
            relationships_map,
            nutrient_map
        )

        if child_tree:
            children.append(child_tree)

    return {
        "id": str(nutrient.id),
        "name": nutrient.name,
        "slug": nutrient.slug,
        "children": children
    }


def get_nutrient_tree(
    db: Session,
    root_slug: str
):

    nutrients = db.query(Nutrient).all()

    relationships = (
        db.query(NutrientRelationship)
        .all()
    )

    nutrient_map = {
        nutrient.id: nutrient
        for nutrient in nutrients
    }

    slug_map = {
        nutrient.slug: nutrient
        for nutrient in nutrients
    }

    relationships_map = {}

    for relationship in relationships:

        parent_id = relationship.parent_nutrient_id

        if parent_id not in relationships_map:
            relationships_map[parent_id] = []

        relationships_map[parent_id].append(
            relationship
        )

    root_nutrient = slug_map.get(root_slug)

    if not root_nutrient:
        return None

    return build_nutrient_tree(
        root_nutrient.id,
        relationships_map,
        nutrient_map
    )
