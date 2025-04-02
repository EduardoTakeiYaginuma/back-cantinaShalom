# app/Compra/compra_repository.py
from app import db
from app.models import Compra

class CompraRepository:
    
    @staticmethod
    def get_all_compras():
        return Compra.query.all()
    
    @staticmethod
    def get_compra_by_id(compra_id):
        return Compra.query.get(compra_id)
    
    @staticmethod
    def create_compra(data):
        nova_compra = Compra(
            total=data['total'],
            data=data['data'],
            usuario_id=data['usuario_id'],
            produto_id=data['produto_id']
        )
        db.session.add(nova_compra)
        db.session.commit()
        return nova_compra
    
    @staticmethod
    def update_compra(compra_id, data):
        compra = Compra.query.get(compra_id)
        if compra:
            compra.total = data['total']
            compra.data = data['data']
            compra.usuario_id = data['usuario_id']
            compra.produto_id = data['produto_id']
            db.session.commit()
            return compra
        return None
    
    @staticmethod
    def delete_compra(compra_id):
        compra = Compra.query.get(compra_id)
        if compra:
            db.session.delete(compra)
            db.session.commit()
            return compra
        return None
