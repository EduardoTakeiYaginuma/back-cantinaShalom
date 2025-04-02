# app/Compra/compra_routes.py
from flask import Blueprint
from app.Compra_Produto.compraProdutoController import CompraProdutoController

compra_bp = Blueprint('compraProduto', __name__)

# Adiciona as rotas do Controller para o blueprint
compra_bp.add_url_rule('/compraProduto', view_func=CompraProdutoController.get_compraProduto, methods=['GET'])
compra_bp.add_url_rule('/compraProduto/<int:compraProduto_id>', view_func=CompraProdutoController.get_compraProduto, methods=['GET'])
compra_bp.add_url_rule('/compraProduto', view_func=CompraProdutoController.create_compraProduto, methods=['POST'])
compra_bp.add_url_rule('/compraProduto/<int:compraProduto_id>', view_func=CompraProdutoController.update_compraProduto, methods=['PUT'])
compra_bp.add_url_rule('/compraProduto/<int:compraProduto_id>', view_func=CompraProdutoController.delete_compraProduto, methods=['DELETE'])
