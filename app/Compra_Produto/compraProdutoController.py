from flask import jsonify, request
from app.Compra_Produto.compraProdutoService import CompraProdutoService


class CompraProdutoController:
    
    @staticmethod
    def get_compraProdutos():
        compraProdutos = CompraProdutoService.get_all_compraProduto()
        return jsonify([{'id': c.id, 'compra_id': c.compra_id, 'produto_id': c.produto_id, 'quantidade': c.quantidade, 'total': c.total} for c in compraProdutos])

    @staticmethod
    def get_compraProduto(compraProduto_id):
        compraProduto = CompraProdutoService.get_compraProduto_by_id(compraProduto_id)
        if compraProduto:
            return jsonify({'id': compraProduto.id, 'compra_id': compraProduto.compra_id, 'produto_id': compraProduto.produto_id, 'quantidade': compraProduto.quantidade, 'total': compraProduto.total})
        return jsonify({'message': 'CompraProduto não encontrado'}), 404

    @staticmethod
    def create_compraProduto():
        data = request.json
        compraProduto = CompraProdutoService.create_compraProduto(data)
        return jsonify(
            {'id': compraProduto.id, 
             'compra_id': compraProduto.compra_id, 
             'produto_id': compraProduto.produto_id, 
             'quantidade': compraProduto.quantidade, 
             'total': compraProduto.total
             }), 201

    @staticmethod
    def update_compraProduto(compraProduto_id):
        data = request.json
        compraProduto = CompraProdutoService.update_compraProduto(compraProduto_id, data)
        if compraProduto:
            return jsonify({'id': compraProduto.id, 'compra_id': compraProduto.compra_id, 'produto_id': compraProduto.produto_id, 'quantidade': compraProduto.quantidade, 'total': compraProduto.total})
        return jsonify({'message': 'CompraProduto não encontrado'}), 404

    @staticmethod
    def delete_compraProduto(compraProduto_id):
        compraProduto = CompraProdutoService.delete_compraProduto(compraProduto_id)
        if compraProduto:
            return jsonify({'message': 'CompraProduto deletado com sucesso'}), 200
        return jsonify({'message': 'CompraProduto não encontrado'}), 404
