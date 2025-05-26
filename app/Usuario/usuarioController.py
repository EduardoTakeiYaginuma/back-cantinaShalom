# app/Usuario/usuario_controller.py
from flask import request, jsonify, Response
from app.Usuario.usuarioService import UsuarioService
from app.model import ResponseEntity

class UsuarioController:

    @staticmethod
    def get_usuarios():
        usuarios = UsuarioService.get_all_usuarios()
        return Response(200, jsonify([u.__dict__ for u in usuarios]))

    @staticmethod
    def create_usuario():
        data = request.json
        usuario = UsuarioService.create_usuario(data)
        return jsonify({'id': usuario.id, 'nome': usuario.nome, 'sobrenome': usuario.sobrenome, 'quarto': usuario.quarto, 'tipo_usuario': usuario.tipo_usuario}), 201

    @staticmethod
    def get_usuario(usuario_id):
        usuario = UsuarioService.get_usuario_by_id(usuario_id)
        if usuario:
            return jsonify({'id': usuario.id, 'nome': usuario.nome, 'sobrenome': usuario.sobrenome, 'saldo': usuario.saldo})
        return jsonify({'message': 'Usuário não encontrado'}), 404
    
    @staticmethod
    def update_usuario(usuario_id):
        data = request.json
        usuario = UsuarioService.update_usuario(usuario_id, data)
        if usuario:
            return jsonify({'id': usuario.id, 'nome': usuario.nome, 'sobrenome': usuario.sobrenome, 'saldo': usuario.saldo})
        return jsonify({'message': 'Usuário não encontrado'}), 404
    
    @staticmethod   
    def delete_usuario(usuario_id):
        usuario = UsuarioService.delete_usuario(usuario_id)
        if usuario:
            return jsonify({'message': 'Usuário deletado com sucesso'}), 200
        return jsonify({'message': 'Usuário não encontrado'}), 404
    