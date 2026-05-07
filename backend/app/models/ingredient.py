from sqlalchemy import (
    Column,
    String,
    DateTime
)

from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.orm import relationship

import uuid

from app.database import Base


class Ingredient(Base):
    __tablename__ = "ingredients"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    name = Column(
        String,
        nullable=False
    )

    created_at = Column(DateTime)

    updated_at = Column(DateTime)

    nutrient_values = relationship(
        "IngredientNutrient",
        back_populates="ingredient"
    )
