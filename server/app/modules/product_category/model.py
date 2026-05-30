from typing import TYPE_CHECKING
from sqlmodel import SQLModel, Relationship, Field

if TYPE_CHECKING:
    from app.modules.category.model import Category
    from app.modules.product.model import Product


class ProductCategory(SQLModel, table=True):
    __tablename__ = "product_category"  # type: ignore

    product_id: int = Field(primary_key=True, foreign_key="product.id")
    category_id: int = Field(primary_key=True, foreign_key="category.id")

    product: "Product" = Relationship(back_populates="product_links")
    category: "Category" = Relationship(back_populates="category_links")
