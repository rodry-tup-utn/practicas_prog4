from sqlmodel import Session
from app.modules.category.model import Category
from app.core.repository import BaseRepository


class CategoryRepository(BaseRepository[Category]):
    def __init__(self, session: Session):
        super().__init__(session, Category)
