# app/Produto/produto_controller.py
from flask import jsonify, request
from app.Produto.produtoService import ProdutoService

class ProdutoController:
    
    @staticmethod
    def get_produtos():
        produtos = ProdutoService.get_all_produtos()
        return jsonify([{'id': p.id, 'nome': p.nome, 'quantidade': p.quantidade, 'tipo': p.tipo, 'preco': p.preco} for p in produtos])

    @staticmethod
    def get_produto(produto_id):
        produto = ProdutoService.get_produto_by_id(produto_id)
        if produto:
            return jsonify({'id': produto.id, 'nome': produto.nome, 'quantidade': produto.quantidade, 'tipo': produto.tipo,'preco': produto.preco})
        return jsonify({'message': 'Produto não encontrado'}), 404

    @staticmethod
    def create_produto():
        data = request.json
        produto = ProdutoService.create_produto(data)
        return jsonify({'id': produto.id, 'nome': produto.nome, 'tipo': produto.tipo, 'quantidade': produto.quantidade, 'preco': produto.preco}), 201

    @staticmethod
    def update_produto(produto_id):
        data = request.json
        produto = ProdutoService.update_produto(produto_id, data)
        if produto:
            return jsonify({'id': produto.id, 'nome': produto.nome, 'quantidade': produto.quantidade, 'preco': produto.preco})
        return jsonify({'message': 'Produto não encontrado'}), 404

    @staticmethod
    def delete_produto(produto_id):
        produto = ProdutoService.delete_produto(produto_id)
        if produto:
            return jsonify({'message': 'Produto deletado com sucesso'}), 200
        return jsonify({'message': 'Produto não encontrado'}), 404
