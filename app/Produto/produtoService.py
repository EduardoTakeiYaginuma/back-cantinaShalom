# app/Produto/produto_service.py
from app.Produto.produtoRepository import ProdutoRepository

class ProdutoService:
    @staticmethod
    def get_all_produtos():
        return ProdutoRepository.get_all()

    @staticmethod
    def get_produto_by_id(produto_id):
        return ProdutoRepository.get_by_id(produto_id)

    @staticmethod
    def create_produto(data):
        return ProdutoRepository.create(data)

    @staticmethod
    def update_produto(produto_id, data):
        return ProdutoRepository.update(produto_id, data)

    @staticmethod
    def delete_produto(produto_id):
        return ProdutoRepository.delete(produto_id)
