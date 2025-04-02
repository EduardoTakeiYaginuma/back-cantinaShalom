# app/Usuario/usuario_service.py
from app.Usuario.usuarioRepository import UsuarioRepository

class UsuarioService:

    @staticmethod
    def get_all_usuarios():
        return UsuarioRepository.get_all()

    @staticmethod
    def create_usuario(data):
        return UsuarioRepository.create(data)
    
    @staticmethod
    def get_usuario_by_id(usuario_id):
        return UsuarioRepository.get_by_id(usuario_id)
    
    @staticmethod
    def update_usuario(usuario_id, data):
        usuario = UsuarioRepository.get_by_id(usuario_id)
        if not usuario:
            raise ValueError("Usuário não encontrado")
        return UsuarioRepository.update(usuario, data)
    
    @staticmethod
    def delete_usuario(usuario_id):
        usuario = UsuarioRepository.get_by_id(usuario_id)
        if not usuario:
            raise ValueError("Usuário não encontrado")
        return UsuarioRepository.delete(usuario)
