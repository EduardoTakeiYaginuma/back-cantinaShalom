# app/Compra/compra_controller.py
from flask import jsonify, request
from app.Compra.compraService import CompraService

class CompraController:
    
    @staticmethod
    def get_compras():
        compras = CompraService.get_all_compras()
        return jsonify([{'id': c.id, 'total': c.total, 'data': c.data, 'usuario_id': c.usuario_id, 'produto_id': c.produto_id} for c in compras])

    @staticmethod
    def get_compra(compra_id):
        compra = CompraService.get_compra_by_id(compra_id)
        if compra:
            return jsonify({'id': compra.id, 'total': compra.total, 'data': compra.data, 'usuario_id': compra.usuario_id, 'produto_id': compra.produto_id})
        return jsonify({'message': 'Compra não encontrada'}), 404

    @staticmethod
    def create_compra():
        data = request.json
        compra = CompraService.create_compra(data)
        return jsonify({'id': compra.id, 'total': compra.total, 'data': compra.data, 'usuario_id': compra.usuario_id, 'produto_id': compra.produto_id}), 201

    @staticmethod
    def update_compra(compra_id):
        data = request.json
        compra = CompraService.update_compra(compra_id, data)
        if compra:
            return jsonify({'id': compra.id, 'total': compra.total, 'data': compra.data, 'usuario_id': compra.usuario_id, 'produto_id': compra.produto_id})
        return jsonify({'message': 'Compra não encontrada'}), 404

    @staticmethod
    def delete_compra(compra_id):
        compra = CompraService.delete_compra(compra_id)
        if compra:
            return jsonify({'message': 'Compra deletada com sucesso'}), 200
        return jsonify({'message': 'Compra não encontrada'}), 404
