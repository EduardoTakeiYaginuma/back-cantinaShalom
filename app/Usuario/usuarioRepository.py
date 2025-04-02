# app/Usuario/usuario_repository.py
from app import db
from app.models import Usuario 

class UsuarioRepository:

    @staticmethod
    def get_all():
        return Usuario.query.all()  

    @staticmethod
    def create(data):
        usuario = Usuario(nome=data['nome'], sobrenome=data['sobrenome'], tipo_usuario=data['tipo_usuario'], saldo=data['saldo'])
        db.session.add(usuario)
        db.session.commit()
        return usuario
