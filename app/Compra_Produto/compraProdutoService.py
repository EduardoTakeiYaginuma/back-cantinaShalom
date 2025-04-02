from app.models import CompraProduto
from app.Compra_Produto.compraProdutoRepository import CompraProdutoRepository
from app.Compra.compraController import CompraController
from app.Produto.produtoController import ProdutoController

class CompraProdutoService:
    
    @staticmethod
    def get_all_compraProduto():
        return CompraProdutoRepository.get_all()

    @staticmethod
    def get_compraProduto_by_id(compraProduto_id):
        return CompraProdutoRepository.get_by_id(compraProduto_id)

    @staticmethod
    def create_compraProduto(data):
        compra = CompraController.get_compra(data['compra_id'])
        produto = ProdutoController.get_produto(data['produto_id'])
        if not compra or not produto:
            return None
        produto = produto.get_json()
        nova_compraProduto = CompraProduto(
            compra_id=data['compra_id'],
            produto_id=data['produto_id'],
            quantidade=data['quantidade'],
            total=produto["preco"] * data['quantidade']  
        )
        return CompraProdutoRepository.create(nova_compraProduto)

    @staticmethod
    def update_compraProduto(compraProduto_id, data):
        compraProduto = CompraProdutoRepository.get_by_id(compraProduto_id)
        if not compraProduto:
            return None
        
        compraProduto["compra_id"] = data['compra_id']
        compraProduto["produto_id"] = data['produto_id']
        compraProduto["quantidade"] = data['quantidade']
        compraProduto["total"] = data['total']

        
        CompraProdutoRepository.update()
        return compraProduto

    @staticmethod
    def delete_compraProduto(compraProduto_id):
        compraProduto = CompraProdutoRepository.get_by_id(compraProduto_id)
        if not compraProduto:
            return None
        
        CompraProdutoRepository.delete(compraProduto)
        return compraProduto
