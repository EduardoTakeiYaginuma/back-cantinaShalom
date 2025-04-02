# app/Usuario/usuario_service.py
from app.Usuario.usuarioRepository import UsuarioRepository

class UsuarioService:

    @staticmethod
    def get_all_usuarios():
        return UsuarioRepository.get_all()

    @staticmethod
    def create_usuario(data):
        return UsuarioRepository.create(data)
