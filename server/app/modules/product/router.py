from fastapi import APIRouter, Depends
from app.modules.product.schemas import (
    ProductCreate,
    ProductUpdate,
    ProductFilters,
    ProductDetail,
    ProductPaginated,
)
from app.modules.product.service import ProductService
from app.core.unit_of_work import get_uow, UnitOfWork

router = APIRouter(prefix="/products", tags=["products"])


def get_service(uow: UnitOfWork = Depends(get_uow)) -> ProductService:
    return ProductService(uow)


@router.get("/", response_model=ProductPaginated)
def list_products(
    filters: ProductFilters = Depends(),
    service: ProductService = Depends(get_service),
):
    return service.list_all(filters)


@router.get("/{id}", response_model=ProductDetail)
def get_product(id: int, service: ProductService = Depends(get_service)):
    return service.get_by_id(id)


@router.post("/", response_model=ProductDetail, status_code=201)
def create_product(
    data: ProductCreate,
    service: ProductService = Depends(get_service),
):
    return service.create(data)


@router.put("/{id}", response_model=ProductDetail)
def update_product(
    id: int,
    data: ProductUpdate,
    service: ProductService = Depends(get_service),
):
    return service.update(id, data)


@router.delete("/{id}", status_code=204)
def delete_product(id: int, service: ProductService = Depends(get_service)):
    service.delete(id)
