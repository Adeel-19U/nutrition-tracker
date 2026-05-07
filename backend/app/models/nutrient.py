from sqlalchemy import (
    Column,
    String,
    Boolean,
    Numeric,
    Integer,
    ForeignKey,
    DateTime
)

from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.orm import relationship

import uuid

from app.database import Base


class Nutrient(Base):
    __tablename__ = "nutrients"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    name = Column(String, nullable=False)

    slug = Column(String, unique=True, nullable=False)

    description = Column(String)

    display_name = Column(String)

    display_order = Column(Integer)

    is_essential = Column(Boolean, default=False)

    daily_recommended_value = Column(Numeric)

    created_at = Column(DateTime)

    updated_at = Column(DateTime)

    category_id = Column(
        UUID(as_uuid=True),
        ForeignKey("nutrient_categories.id"),
        nullable=False
    )

    group_id = Column(
        UUID(as_uuid=True),
        ForeignKey("nutrient_groups.id"),
        nullable=False
    )

    unit_id = Column(
        UUID(as_uuid=True),
        ForeignKey("units.id"),
        nullable=False
    )

    category = relationship("NutrientCategory")

    group = relationship("NutrientGroup")

    unit = relationship("Unit")

    aliases = relationship(
        "NutrientAlias",
        back_populates="nutrient"
    )

    tag_mappings = relationship(
        "NutrientTagMapping",
        back_populates="nutrient"
    )
    