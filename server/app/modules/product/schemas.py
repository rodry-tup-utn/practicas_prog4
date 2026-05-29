from sqlmodel import SQLModel, Field
from decimal import Decimal


class ProductoCreate(SQLModel):
    name: str = Field(min_length=3, max_length=80)
    description: str | None = Field(default=None, min_length=3, max_length=255)
    base_price: Decimal = Field(gt=0)
    image_url: list[str] | None = []
    category_ids: list[int] = []


class ProductoUpdate(SQLModel):
    name: str | None = None
    description: str | None = None
    base_price: Decimal | None = Field(default=None, gt=0)
    active: bool | None = None


class ProductoRead(SQLModel):
    id: int
    name: str
    description: str | None
    base_price: Decimal


class UpdateActive(SQLModel):
    active: bool


class CategoriaBasicRead(SQLModel):
    id: int
    name: str


class ProductDetail(ProductoRead):
    categories: list[CategoriaBasicRead]


class ProductFilters(SQLModel):
    name: str | None = Field(default=None, min_length=3, max_length=80)
    min_price: Decimal | None = Field(default=None, ge=0)
    max_price: Decimal | None = Field(default=None, ge=0)
    active: bool | None = None
    category_id: int | None = None
