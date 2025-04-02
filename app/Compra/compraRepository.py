# app/Compra/compra_repository.py
from app import db
from app.models import Compra
from datetime import date

class CompraRepository:
    
    @staticmethod
    def get_all_compras():
        return Compra.query.all()
    
    @staticmethod
    def get_compra_by_id(compra_id):
        return Compra.query.get(compra_id)
    
    @staticmethod
    def create_compra(data):
        compra = Compra(
            total= 0,
            data=date.today(),
            usuario_id=data['usuario_id'],
        )
        db.session.add(compra)
        db.session.commit()
        return compra
    
    @staticmethod
    def update_compra(compra, data):
        compra["usuario_id"] = data['usuario_id']
        compra["total"] = data['total']
        db.session.add(compra)  
        db.session.commit()
        return compra
    
    @staticmethod
    def delete_compra(compra):  
        db.session.delete(compra)
        db.session.commit()
        return compra

