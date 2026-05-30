from fastapi import HTTPException, status
from app.modules.category.model import Category
from app.modules.category.schemas import (
    CategoryCreate,
    CategoryUpdate,
    CategoryPaginated,
    CategoryFilters,
    CategoryRead,
)
from app.core.unit_of_work import UnitOfWork


class CategoryService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    def list_all(self, filters: CategoryFilters) -> CategoryPaginated:
        data = self.uow.categories.get_all(filters)
        total = self.uow.categories.count(filters)

        items = [CategoryRead.model_validate(c) for c in data]

        return CategoryPaginated(items=items, total=total)

    def _get_or_404(self, id: int):
        category = self.uow.categories.get_by_id(id)
        if not category:
            raise HTTPException(
                status.HTTP_404_NOT_FOUND, f"Categoria {id} no encontrada"
            )
        return category

    def get_by_id(self, id: int) -> Category | None:
        return self._get_or_404(id)

    def create(self, data: CategoryCreate) -> Category:
        category = Category.model_validate(data)
        self.uow.categories.add(category)
        return category

    def update(self, id: int, data: CategoryUpdate) -> Category:
        category = self._get_or_404(id)
        update_data = data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(category, key, value)
        self.uow.session.refresh(category)
        return category

    def delete(self, id: int) -> None:
        category = self._get_or_404(id)
        self.uow.categories.delete(category)
