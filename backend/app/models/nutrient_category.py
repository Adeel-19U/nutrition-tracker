from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.dialects.postgresql import UUID

import uuid

from app.database import Base


class NutrientCategory(Base):
    __tablename__ = "nutrient_categories"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    name = Column(String, nullable=False)

    slug = Column(String, unique=True, nullable=False)

    display_order = Column(Integer)

    created_at = Column(DateTime)

    updated_at = Column(DateTime)
