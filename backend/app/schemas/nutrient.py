from pydantic import BaseModel
from uuid import UUID


class NutrientCategoryResponse(BaseModel):
    id: UUID
    name: str
    slug: str

    class Config:
        from_attributes = True


class NutrientGroupResponse(BaseModel):
    id: UUID
    name: str
    slug: str

    class Config:
        from_attributes = True


class UnitResponse(BaseModel):
    id: UUID
    name: str
    symbol: str

    class Config:
        from_attributes = True


class NutrientAliasResponse(BaseModel):
    id: UUID
    alias: str

    class Config:
        from_attributes = True


class NutrientTagResponse(BaseModel):
    id: UUID
    name: str
    slug: str

    class Config:
        from_attributes = True


class NutrientResponse(BaseModel):
    id: UUID

    name: str

    slug: str

    display_name: str | None

    description: str | None

    is_essential: bool

    daily_recommended_value: float | None

    category: NutrientCategoryResponse

    group: NutrientGroupResponse

    unit: UnitResponse

    aliases: list[NutrientAliasResponse]

    tags: list[NutrientTagResponse] = []

    class Config:
        from_attributes = True
