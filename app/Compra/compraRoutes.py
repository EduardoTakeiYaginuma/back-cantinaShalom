# app/Compra/compra_routes.py
from flask import Blueprint
from app.Compra.compraController import CompraController

compra_bp = Blueprint('compra', __name__)

# Adiciona as rotas do Controller para o blueprint
compra_bp.add_url_rule('/compras', view_func=CompraController.get_compras, methods=['GET'])
compra_bp.add_url_rule('/compras/<int:compra_id>', view_func=CompraController.get_compra, methods=['GET'])
compra_bp.add_url_rule('/compras', view_func=CompraController.create_compra, methods=['POST'])
compra_bp.add_url_rule('/compras/<int:compra_id>', view_func=CompraController.update_compra, methods=['PUT'])
compra_bp.add_url_rule('/compras/<int:compra_id>', view_func=CompraController.delete_compra, methods=['DELETE'])
