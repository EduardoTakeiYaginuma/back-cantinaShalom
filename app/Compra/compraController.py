# app/Compra/compra_controller.py
from flask import jsonify, request, Response
from app.Compra.compraService import CompraService
from app.model import ResponseEntity

class CompraController:
    
    @staticmethod
    def get_compras():
        compras = CompraService.get_all_compras()
        return Response(200, "Compras recuperadas com sucesso", [{'id': c.id, 'total': c.total, 'data': c.data, 'usuario_id': c.usuario_id} for c in compras])
        # return ResponseEntity(
        #     200,
        #     "Compras recuperadas com sucesso",
        #     [{'id': c.id, 'total': c.total, 'data': c.data, 'usuario_id': c.usuario_id} for c in compras]
        # )

    @staticmethod
    def get_compra(compra_id):
        compra = CompraService.get_compra_by_id(compra_id)
        if compra:
            return ResponseEntity(200, jsonify({'id': compra.id, 'total': compra.total, 'data': compra.data, 'usuario_id': compra.usuario_id}))
        return ResponseEntity(404, jsonify({'message': 'Compra não encontrada'}))

    @staticmethod
    def delete_compra(compra_id):
        compra = CompraService.delete_compra(compra_id)
        if compra:
            return ResponseEntity(200, jsonify({'message': 'Compra deletada com sucesso'}))
        return ResponseEntity(404, jsonify({'message': 'Compra não encontrada'}))

    @staticmethod
    def update_compra(compra_id):
        data = request.json
        compra = CompraService.update_compra(compra_id, data)
        if compra:
            return ResponseEntity(200, jsonify({'id': compra.id, 'total': compra.total, 'data': compra.data, 'usuario_id': compra.usuario_id}))
        return ResponseEntity(404, jsonify({'message': 'Compra não encontrada'}))

    @staticmethod
    def create_compra():
        data = request.json
        compra = CompraService.create_compra(data)
        return ResponseEntity(201, jsonify({'id': compra.id, 'total': compra.total, 'data': compra.data, 'usuario_id': compra.usuario_id}))
