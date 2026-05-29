from fastapi import HTTPException
from app.modules.category.model import Category
from app.modules.category.schemas import CategoryCreate, CategoryUpdate
from app.core.unit_of_work import UnitOfWork


class CategoryService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    def list(self) -> list[Category]:
        return list(self.uow.categories.get_all())

    def get_by_id(self, id: int) -> Category | None:
        return self.uow.categories.get_by_id(id)

    def create(self, data: CategoryCreate) -> Category:
        category = Category.model_validate(data)
        self.uow.categories.add(category)
        self.uow.commit()
        return category

    def update(self, id: int, data: CategoryUpdate) -> Category:
        category = self.uow.categories.get_by_id(id)
        if not category:
            raise HTTPException(status_code=404, detail="Categoría no encontrada")
        update_data = data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(category, key, value)
        self.uow.commit()
        self.uow.session.refresh(category)
        return category

    def delete(self, id: int) -> None:
        category = self.uow.categories.get_by_id(id)
        if not category:
            raise HTTPException(status_code=404, detail="Categoría no encontrada")
        self.uow.categories.delete(category)
        self.uow.commit()
