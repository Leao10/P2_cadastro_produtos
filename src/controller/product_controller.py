from fastapi import APIRouter, Depends, Header

from src.repository.usuario_repository import ProductRepository
from src.config.dependencies import get_authenticated_user, get_product_service
from src.domain.dto.dtos import ProdutoCreateDTO, ProdutoUpdateDTO, ProdutoDTO
from src.service.product_service import ProductService

product_router = APIRouter(prefix='/products', tags=['Products'], dependencies=[Depends(get_authenticated_user)])


@product_router.post(path='/', status_code=201, description='Adiciona um novo produto', response_model=ProdutoDTO)
async def create(request: ProdutoCreateDTO, product_service: ProductService = Depends(get_product_service)):
    return product_service.create(request)


@product_router.get(path='/{user_id}', status_code=200, description='Busca o produto pelo id', response_model=ProdutoDTO)
async def find_by_id(user_id: int, product_service: ProductService = Depends(get_product_service)):
    return product_service.find_by_id(user_id=user_id)


@product_router.get(path='/', status_code=200, description='Busca todos os produtos', response_model=list[ProdutoDTO])
async def find_all(product_service: ProductService = Depends(get_product_service)):
    return product_service.find_all()


@product_router.put(path='/{user_id}', status_code=200, description='Atualiza um produto', response_model=ProdutoDTO)
async def update(user_id: int, user_data: ProdutoUpdateDTO, product_service: ProductService=Depends(get_product_service)):
    return product_service.update(user_id, user_data)


@product_router.delete(path='/{user_id}', status_code=204, description='Exclui o produto pelo id')
async def delete(user_id: int, product_service: ProductService = Depends(get_product_service)):
    product_service.delete(user_id=user_id)