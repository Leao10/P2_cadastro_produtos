import logging

from src.domain.dto.dtos import ProdutoCreateDTO, ProdutoDTO, ProdutoUpdateDTO
from src.repository.usuario_repository import ProductRepository


class ProductService:

    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def create(self, data: ProdutoCreateDTO) -> ProdutoDTO:
        logging.info('Criando produto')
        # TODO: implementar método
        pass

    def find_by_id(self, user_id: int) -> ProdutoDTO:
        logging.info(f'Buscando produto com ID {user_id}')
        # TODO: implementar método
        pass

    def find_all(self) -> list[ProdutoDTO]:
        logging.info('Buscando todos os produtos')
        # TODO: implementar método
        pass

    def update(self, user_id: int, user_data: ProdutoUpdateDTO) -> ProdutoDTO:
        logging.info(f'Atualizando produto com ID {user_id}')
        # TODO: implementar método
        pass

    def delete(self, user_id: int) -> int:
        logging.info(f'Deletando produto com ID {user_id}')
        # TODO: implementar método
        pass
