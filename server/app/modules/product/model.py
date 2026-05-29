from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import JSON
from typing import TYPE_CHECKING
from app.modules.product_category.model import ProductCategory

if TYPE_CHECKING:
    from app.modules.category.model import Category


class Product(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True, min_length=3, max_length=80)
    description: str | None = Field(max_length=255, min_length=3, default=None)
    base_price: float = Field(gt=0)
    image_url: list[str] | None = Field(default=None, sa_type=JSON)
    active: bool = True

    categories: list["Category"] = Relationship(back_populates="products", link_model=ProductCategory)
    product_links: list["ProductCategory"] = Relationship(back_populates="product")
