from sqlalchemy import (
    Column,
    String,
    Numeric,
    DateTime
)

from sqlalchemy.dialects.postgresql import UUID

import uuid

from app.database import Base


class Unit(Base):
    __tablename__ = "units"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    name = Column(String, nullable=False)

    symbol = Column(String, unique=True, nullable=False)

    category = Column(String, nullable=False)

    conversion_to_base = Column(
        Numeric,
        nullable=False
    )

    created_at = Column(DateTime)

    updated_at = Column(DateTime)
