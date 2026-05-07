from sqlalchemy import (
    Column,
    String,
    DateTime
)

from sqlalchemy.dialects.postgresql import UUID

import uuid

from app.database import Base


class NutrientTag(Base):
    __tablename__ = "nutrient_tags"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    name = Column(String, nullable=False)

    slug = Column(String, unique=True, nullable=False)

    description = Column(String)

    created_at = Column(DateTime)

    updated_at = Column(DateTime)
