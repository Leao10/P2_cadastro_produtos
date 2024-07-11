import logging
from sqlite3 import IntegrityError

from fastapi import HTTPException, logger
from pydantic import TypeAdapter

from src.domain.dto.dtos import ProdutoCreateDTO, ProdutoDTO, ProdutoUpdateDTO
from src.domain.model.models import Product
from src.repository.usuario_repository import ProductRepository

logger = logging.getLogger('fastapi')

class ProductService:

    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def create(self, user_data: ProdutoCreateDTO) -> ProdutoDTO:
        logger.info('Criando um novo produto')
        user = Product(**user_data.model_dump())
        try:
            created = self.usuario_repository.save(user)
            return TypeAdapter(ProdutoDTO).validate_python(created)
        except IntegrityError as e:
            logger.error(f'Erro na criação o Produto: {user_data.model_dump()}')
            raise HTTPException(status_code=409, detail=f'Produto já existe: {e.args[0]}')

    def read(self, user_id: int) -> ProdutoDTO:
        logger.info('Buscando produto')
        return TypeAdapter(ProdutoDTO).validate_python(self._read(user_id))

    def _read(self, user_id: int) -> Product:
        user = self.usuario_repository.read(user_id)
        if user is None:
            self.logger.error(f'Produto {user_id}, não foi encontrado')
            raise HTTPException(status_code=404, detail=f'Produto {user_id} não encontrado!')
        return user

    def find_all(self) -> list[ProdutoDTO]:
        logger.info('Buscando todos produtos')
        users = self.usuario_repository.find_all()
        return [TypeAdapter(ProdutoDTO).validate_python(user) for user in users]

    def update(self, user_id: int, user_data: ProdutoUpdateDTO) -> ProdutoDTO:
        logging.info(f'Atualizando produto com ID {user_id}')
        # TODO: implementar método
        pass

    def update(self, user_id: int, user_data: ProdutoUpdateDTO):
        logger.info('Atualizando o produto: {user_id}')
        user = self._read(user_id)
        user_data = user_data.model_dump(exclude_unset=True)
        for key, value in user_data.items():
            setattr(user, key, value)
        user_updated = self.usuario_repository.save(user)
        logger.info(f'Produto {user_id}, foi atualizado: {user_updated}')
        return TypeAdapter(ProdutoDTO).validate_python(user_updated)

    def delete(self, user_id: int) -> int:
        user = self._read(user_id)
        self.usuario_repository.delete(user)
        logger.info(f'Produto {user_id}, foi deletado')
        return user_id
