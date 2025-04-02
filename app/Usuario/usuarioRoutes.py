# app/Usuario/usuario_routes.py
from flask import Blueprint
from app.Usuario.usuarioController import UsuarioController

usuario_bp = Blueprint('usuario', __name__)

# Adiciona as rotas do Controller para o blueprint
usuario_bp.add_url_rule('/usuarios', view_func=UsuarioController.get_usuarios, methods=['GET'])
usuario_bp.add_url_rule('/usuarios', view_func=UsuarioController.create_usuario, methods=['POST'])
usuario_bp.add_url_rule('/usuarios/<int:usuario_id>', view_func=UsuarioController.get_usuario, methods=['GET'])
usuario_bp.add_url_rule('/usuarios/<int:usuario_id>', view_func=UsuarioController.update_usuario, methods=['PUT'])
usuario_bp.add_url_rule('/usuarios/<int:usuario_id>', view_func=UsuarioController.delete_usuario, methods=['DELETE'])

