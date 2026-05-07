from sqlalchemy import (
    Column,
    Numeric,
    DateTime,
    ForeignKey
)

from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.orm import relationship

import uuid

from app.database import Base


class IngredientNutrient(Base):
    __tablename__ = "ingredient_nutrients"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    value_per_100g = Column(
        Numeric,
        nullable=False
    )

    created_at = Column(DateTime)

    updated_at = Column(DateTime)

    ingredient_id = Column(
        UUID(as_uuid=True),
        ForeignKey("ingredients.id"),
        nullable=False
    )

    nutrient_id = Column(
        UUID(as_uuid=True),
        ForeignKey("nutrients.id"),
        nullable=False
    )

    unit_id = Column(
        UUID(as_uuid=True),
        ForeignKey("units.id"),
        nullable=False
    )

    ingredient = relationship(
        "Ingredient",
        back_populates="nutrient_values"
    )

    nutrient = relationship("Nutrient")

    unit = relationship("Unit")
