from sqlmodel import Session, select, col
from sqlalchemy.orm import selectinload
from app.modules.product.model import Product
from app.core.repository import BaseRepository
from app.modules.product.schemas import ProductFilters
from app.modules.product_category.model import ProductCategory


class ProductoRepository(BaseRepository[Product]):
    def __init__(self, session: Session):
        super().__init__(session, Product)

    def get_by_id_with_details(
        self, id: int, incluir_inactivos: bool = False
    ) -> Product | None:
        query = (
            select(Product)
            .where(Product.id == id)
            .options(selectinload(Product.categories))  # type: ignore[arg-type]
        )
        if not incluir_inactivos:
            query = query.where(Product.active)
        return self.session.exec(query).first()

    def get_all(self, filters: ProductFilters | None = None) -> list[Product]:
        query = select(Product).options(
            selectinload(Product.categories)  # type: ignore[arg-type]
        )
        if filters:
            if filters.name:
                query = query.where(col(Product.name).ilike(f"%{filters.name}%"))
            if filters.min_price is not None:

                query = query.where(Product.base_price >= filters.min_price)
            if filters.max_price is not None:
                query = query.where(Product.base_price <= filters.max_price)

            if filters.active:
                query = query.where(Product.active == True)

            if filters.category_id is not None:
                query = query.where(
                    Product.product_links.any(ProductCategory.category_id == filters.category_id)  # type: ignore
                )

        return list(self.session.exec(query).all())

    def save(self, producto: Product) -> Product:
        self.session.commit()
        self.session.refresh(producto)
        return producto
