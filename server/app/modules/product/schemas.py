from decimal import Decimal
from pydantic import Field, BaseModel, ConfigDict


class ProductCreate(BaseModel):
    name: str = Field(min_length=3, max_length=80)
    description: str | None = Field(default=None, min_length=3, max_length=255)
    base_price: Decimal = Field(gt=0)
    image_url: list[str] | None = []
    category_ids: list[int] = []


class ProductUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    base_price: Decimal | None = Field(default=None, gt=0)
    available: bool | None = None


class ProductRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    description: str | None
    base_price: Decimal
    available: bool


class ProductPaginated(BaseModel):
    items: list[ProductRead]
    total: int


class CategoriaBasicRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str


class ProductDetail(ProductRead):
    categories: list[CategoriaBasicRead]


class ProductFilters(BaseModel):
    name: str | None = Field(default=None, min_length=3, max_length=80)
    min_price: Decimal | None = Field(default=None, ge=0)
    max_price: Decimal | None = Field(default=None, ge=0)
    active: bool | None = None
    category_id: int | None = None
    offset: int = 0
    limit: int = 10
    available: bool | None = None
