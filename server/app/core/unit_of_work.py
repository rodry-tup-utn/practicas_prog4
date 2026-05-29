from fastapi import Depends
from sqlmodel import Session
from app.core.database import get_session
from app.modules.product.repository import ProductoRepository
from app.modules.category.repository import CategoryRepository


class UnitOfWork:
    def __init__(self, session: Session):
        self.session = session
        self.products = ProductoRepository(session)
        self.categories = CategoryRepository(session)

    def commit(self) -> None:
        self.session.commit()

    def rollback(self) -> None:
        self.session.rollback()


def get_uow(session: Session = Depends(get_session)):
    uow = UnitOfWork(session)
    try:
        yield uow
        uow.commit()
    except Exception:
        uow.rollback()
        raise
