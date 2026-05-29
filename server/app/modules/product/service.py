from fastapi import HTTPException
from app.modules.product.model import Product
from app.modules.category.model import Category
from app.modules.product.schemas import (
    ProductoCreate,
    ProductoUpdate,
    UpdateActive,
    ProductFilters,
)
from app.core.unit_of_work import UnitOfWork


class ProductoService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    def list(self, filters: ProductFilters | None = None) -> list[Product]:
        return self.uow.products.get_all(filters)

    def get_by_id(self, id: int) -> Product | None:
        return self.uow.products.get_by_id_with_details(id)

    def create(self, data: ProductoCreate) -> Product:
        producto = Product.model_validate(data)
        for cat_id in data.category_ids:
            cat = self.uow.session.get(Category, cat_id)
            if cat:
                producto.categories.append(cat)
        self.uow.products.add(producto)
        self.uow.commit()
        self.uow.session.refresh(producto)
        return producto

    def update(self, id: int, data: ProductoUpdate) -> Product:
        producto = self.uow.products.get_by_id_with_details(id)
        if not producto:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
        update_data = data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(producto, key, value)
        self.uow.products.save(producto)
        return producto

    def update_active(self, id: int, data: UpdateActive) -> Product:
        producto = self.uow.products.get_by_id(id)
        if not producto:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
        producto.active = data.active
        self.uow.products.save(producto)
        return producto

    def delete(self, id: int) -> None:
        producto = self.uow.products.get_by_id(id)
        if not producto:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
        self.uow.products.delete(producto)
        self.uow.commit()
