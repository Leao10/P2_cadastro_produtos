from fastapi import APIRouter, Depends

from src.repository.usuario_repository import ProductRepository
from src.config.dependencies import get_authenticated_user, get_product_service
from src.domain.dto.dtos import ProdutoCreateDTO, ProdutoUpdateDTO, ProdutoDTO
from src.service.product_service import ProductService

product_router = APIRouter(prefix='/products', tags=['Products'], dependencies=[Depends(get_authenticated_user)])


@product_router.post('/', status_code=201, description='Adiciona um novo produto', response_model=ProdutoCreateDTO)
async def create(request: ProdutoCreateDTO, service: ProductService = Depends(get_product_service)):
    product_service = ProductService(service)
    return product_service.create(request)


@product_router.get('/{user_id}', status_code=200, description='Busca o produto pelo id', response_model=ProdutoDTO)
async def find_by_id(user_id: int, service: ProductService = Depends(get_product_service)):
    product_service = ProductService(service)
    return product_service.find_by_id(user_id=user_id)


@product_router.get('/', status_code=200, description='Busca todos os produtos', response_model=list[ProdutoDTO])
async def find_all(service: ProductService = Depends(get_product_service)):
    product_service = ProductService(service)
    return product_service.find_all()


@product_router.put('/{user_id}', status_code=200, description='Atualiza um produto', response_model=ProdutoDTO)
async def update(user_id: int, user_data: ProdutoUpdateDTO, service: ProductService = Depends(get_product_service)):
    product_service = ProductService(service)
    return product_service.update(user_id, user_data)


@product_router.delete('/{user_id}', status_code=204, description='Deleta o produto pelo id')
async def delete(user_id: int, service: ProductService = Depends(get_product_service)):
    product_service = ProductService(service)
    product_service.delete(user_id=user_id)