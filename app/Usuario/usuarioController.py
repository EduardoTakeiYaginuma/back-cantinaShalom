# app/Usuario/usuario_controller.py
from flask import request, jsonify
from app.Usuario.usuarioService import UsuarioService

class UsuarioController:

    @staticmethod
    def get_usuarios():
        usuarios = UsuarioService.get_all_usuarios()
        return jsonify([{'id': u.id, 'nome': u.nome, 'sobrenome': u.sobrenome, 'saldo': u.saldo} for u in usuarios])

    @staticmethod
    def create_usuario():
        data = request.json
        usuario = UsuarioService.create_usuario(data)
        return jsonify({'id': usuario.id, 'nome': usuario.nome, 'sobrenome': usuario.sobrenome}), 201
