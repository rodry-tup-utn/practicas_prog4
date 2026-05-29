from fastapi import APIRouter, Depends
from app.modules.product.schemas import (
    ProductoCreate,
    ProductoUpdate,
    UpdateActive,
    ProductFilters,
    ProductDetail,
)
from fastapi import HTTPException
from app.modules.product.service import ProductoService
from app.core.unit_of_work import get_uow, UnitOfWork

router = APIRouter(prefix="/products", tags=["products"])


def get_service(uow: UnitOfWork = Depends(get_uow)) -> ProductoService:
    return ProductoService(uow)


@router.get("/", response_model=list[ProductDetail])
def list_products(
    filters: ProductFilters = Depends(),
    service: ProductoService = Depends(get_service),
):
    return service.list(filters)


@router.get("/{id}", response_model=ProductDetail)
def get_product(id: int, service: ProductoService = Depends(get_service)):
    product = service.get_by_id(id)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return product


@router.post("/", response_model=ProductDetail, status_code=201)
def create_product(
    data: ProductoCreate,
    service: ProductoService = Depends(get_service),
):
    return service.create(data)


@router.put("/{id}", response_model=ProductDetail)
def update_product(
    id: int,
    data: ProductoUpdate,
    service: ProductoService = Depends(get_service),
):
    return service.update(id, data)


@router.patch("/{id}/active", response_model=ProductDetail)
def update_active(
    id: int,
    data: UpdateActive,
    service: ProductoService = Depends(get_service),
):
    return service.update_active(id, data)


@router.delete("/{id}", status_code=204)
def delete_product(id: int, service: ProductoService = Depends(get_service)):
    service.delete(id)
