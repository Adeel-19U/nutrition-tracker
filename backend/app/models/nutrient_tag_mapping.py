from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey
)

from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.orm import relationship

import uuid

from app.database import Base


class NutrientTagMapping(Base):
    __tablename__ = "nutrient_tag_mappings"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    created_at = Column(DateTime)

    nutrient_id = Column(
        UUID(as_uuid=True),
        ForeignKey("nutrients.id"),
        nullable=False
    )

    tag_id = Column(
        UUID(as_uuid=True),
        ForeignKey("nutrient_tags.id"),
        nullable=False
    )

    nutrient = relationship(
        "Nutrient",
        back_populates="tag_mappings"
    )

    tag = relationship("NutrientTag")
