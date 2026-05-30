from fastapi import HTTPException, status
from app.modules.product.model import Product
from app.modules.category.model import Category
from app.modules.product.schemas import (
    ProductCreate,
    ProductUpdate,
    ProductFilters,
    ProductPaginated,
    ProductRead,
)
from app.core.unit_of_work import UnitOfWork


class ProductService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    def list_all(self, filters: ProductFilters) -> ProductPaginated:
        data = self.uow.products.get_all(filters)
        total = self.uow.products.count(filters)
        items = [ProductRead.model_validate(p) for p in data]

        return ProductPaginated(items=items, total=total)

    def _get_or_404(self, id: int):
        product = self.uow.products.get_by_id_with_details(id)
        if not product:
            raise HTTPException(
                status.HTTP_404_NOT_FOUND, f"Producto id {id} no encontrado"
            )
        return product

    def get_by_id(self, id: int) -> Product | None:
        product = self._get_or_404(id)

        return product

    def create(self, data: ProductCreate) -> Product:
        product = Product.model_validate(data)
        for cat_id in data.category_ids:
            cat = self.uow.session.get(Category, cat_id)
            if cat:
                product.categories.append(cat)
        self.uow.products.add(product)
        self.uow.session.refresh(product)
        return product

    def update(self, id: int, data: ProductUpdate) -> Product:
        product = self._get_or_404(id)
        update_data = data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(product, key, value)
        self.uow.products.add(product)
        return product

    def delete(self, id: int) -> None:
        producto = self._get_or_404(id)

        self.uow.products.delete(producto)
