from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING
from app.modules.product_category.model import ProductCategory

if TYPE_CHECKING:
    from app.modules.product.model import Product


class Category(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(unique=True, index=True, min_length=3, max_length=40)
    description: str | None = Field(default=None, min_length=3, max_length=255)

    products: list["Product"] = Relationship(back_populates="categories", link_model=ProductCategory)
    category_links: list["ProductCategory"] = Relationship(back_populates="category_link")
