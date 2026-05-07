from sqlalchemy import (
    Column,
    String,
    DateTime,
    ForeignKey
)

from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.orm import relationship

import uuid

from app.database import Base


class NutrientAlias(Base):
    __tablename__ = "nutrient_aliases"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    alias = Column(String, nullable=False)

    created_at = Column(DateTime)

    updated_at = Column(DateTime)

    nutrient_id = Column(
        UUID(as_uuid=True),
        ForeignKey("nutrients.id"),
        nullable=False
    )

    nutrient = relationship(
        "Nutrient",
        back_populates="aliases"
    )
