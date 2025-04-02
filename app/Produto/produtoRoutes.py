# app/Produto/produto_routes.py
from flask import Blueprint
from app.Produto.produtoController import ProdutoController

produto_bp = Blueprint('produto', __name__)

# Adiciona as rotas do Controller para o blueprint
produto_bp.add_url_rule('/produtos', view_func=ProdutoController.get_produtos, methods=['GET'])
produto_bp.add_url_rule('/produtos/<int:produto_id>', view_func=ProdutoController.get_produto, methods=['GET'])
produto_bp.add_url_rule('/produtos', view_func=ProdutoController.create_produto, methods=['POST'])
produto_bp.add_url_rule('/produtos/<int:produto_id>', view_func=ProdutoController.update_produto, methods=['PUT'])
produto_bp.add_url_rule('/produtos/<int:produto_id>', view_func=ProdutoController.delete_produto, methods=['DELETE'])
