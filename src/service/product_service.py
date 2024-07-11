import logging
from sqlite3 import IntegrityError

from fastapi import HTTPException, logger
from pydantic import TypeAdapter

from src.domain.dto.dtos import ProdutoCreateDTO, ProdutoDTO, ProdutoUpdateDTO
from src.domain.model.models import Product
from src.repository.usuario_repository import ProductRepository

class ProductService:

    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def create(self, data: ProdutoCreateDTO) -> ProdutoDTO:
        logging.info('Criando um novo produto')
        produto = Product(**data.model_dump())
        try:
            created = self.usuario_repository.save(produto)
            return TypeAdapter(ProdutoDTO).validate_python(created)
        except IntegrityError as e:
            logger.error(f'Erro na criação o Produto: {data.model_dump()}')
            raise HTTPException(status_code=409, detail=f'Produto já existe: {e.args[0]}')

    def read(self, user_id: int) -> ProdutoDTO:
        logging.info('Buscando produto')
        return TypeAdapter(ProdutoDTO).validate_python(self._read(user_id))

    def _read(self, user_id: int) -> Product:
        produto = self.usuario_repository.read(user_id)
        if produto is None:
            logging.error(f'Produto {user_id}, não foi encontrado')
            raise HTTPException(status_code=404, detail=f'Produto {user_id} não encontrado!')
        return produto

    def find_all(self) -> list[ProdutoDTO]:
        logging.info('Buscando todos produtos')
        produtos = self.repository.find_all()
        return [TypeAdapter(ProdutoDTO).validate_python(produto) for produto in produtos]

    def update(self, user_id: int, user_data: ProdutoUpdateDTO):
        logging.info('Atualizando o produto: {user_id}')
        produto = self._read(user_id)
        data = user_data.model_dump(exclude_unset=True)
        for key, value in user_data.items():
            setattr(produto, key, value)
        produto_updated = self.repository.save(produto)
        logging.info(f'Produto {user_id}, foi atualizado: {produto_updated}')
        return TypeAdapter(ProdutoDTO).validate_python(produto_updated)

    def delete(self, user_id: int) -> int:
        produto = self._read(user_id)
        self.repository.delete(produto)
        logging.info(f'Produto {user_id}, foi deletado')
        return user_id
