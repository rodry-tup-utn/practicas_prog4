from sqlmodel import Session, col, select
from app.modules.category.model import Category
from app.core.repository import BaseRepository
from app.modules.category.schemas import CategoryFilters
from sqlalchemy import func


class CategoryRepository(BaseRepository[Category]):
    def __init__(self, session: Session):
        super().__init__(session, Category)

    def _apply_filters(self, query, filters: CategoryFilters):
        if filters.name:
            query = query.where(col(Category.name).ilike(f"%{filters.name}"))

        return query

    def get_all(self, filters: CategoryFilters) -> list[Category]:
        query = select(Category)

        query = self._apply_filters(query, filters)

        query = query.offset(filters.offset).limit(filters.limit)

        items = self.session.exec(query).all()

        return list(items)

    def count(self, filters) -> int:
        query = select(func.count()).select_from(Category)
        query = self._apply_filters(query, filters)

        return self.session.exec(query).one()
