from sqlalchemy import (
    Column,
    String,
    DateTime,
    ForeignKey
)

from sqlalchemy.dialects.postgresql import UUID

import uuid

from app.database import Base


class NutrientRelationship(Base):
    __tablename__ = "nutrient_relationships"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    relationship_type = Column(
        String,
        nullable=False
    )

    created_at = Column(DateTime)

    updated_at = Column(DateTime)

    parent_nutrient_id = Column(
        UUID(as_uuid=True),
        ForeignKey("nutrients.id"),
        nullable=False
    )

    child_nutrient_id = Column(
        UUID(as_uuid=True),
        ForeignKey("nutrients.id"),
        nullable=False
    )
