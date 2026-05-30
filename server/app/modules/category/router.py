from fastapi import APIRouter, Depends
from app.modules.category.schemas import (
    CategoryCreate,
    CategoryUpdate,
    CategoryRead,
    CategoryFilters,
    CategoryPaginated,
)
from app.modules.category.service import CategoryService
from app.core.unit_of_work import get_uow, UnitOfWork

router = APIRouter(prefix="/categories", tags=["categories"])


def get_service(uow: UnitOfWork = Depends(get_uow)) -> CategoryService:
    return CategoryService(uow)


@router.get("/", response_model=CategoryPaginated)
def list_categories(
    filters: CategoryFilters = Depends(),
    service: CategoryService = Depends(get_service),
):
    return service.list_all(filters)


@router.get("/{id}", response_model=CategoryRead)
def get_category(id: int, service: CategoryService = Depends(get_service)):
    return service.get_by_id(id)


@router.post("/", response_model=CategoryRead, status_code=201)
def create_category(
    data: CategoryCreate,
    service: CategoryService = Depends(get_service),
):
    return service.create(data)


@router.patch("/{id}", response_model=CategoryRead)
def update_category(
    id: int,
    data: CategoryUpdate,
    service: CategoryService = Depends(get_service),
):
    return service.update(id, data)


@router.delete("/{id}", status_code=204)
def delete_category(id: int, service: CategoryService = Depends(get_service)):
    service.delete(id)
