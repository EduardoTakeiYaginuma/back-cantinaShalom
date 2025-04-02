# app/Compra/compra_service.py
from app.Compra.compraRepository import CompraRepository

class CompraService:
    
    @staticmethod
    def get_all_compras():
        return CompraRepository.get_all_compras()
    
    @staticmethod
    def get_compra_by_id(compra_id):
        return CompraRepository.get_compra_by_id(compra_id)
    
    @staticmethod
    def create_compra(data):
        return CompraRepository.create_compra(data)
    
    @staticmethod
    def update_compra(compra_id, data):
        return CompraRepository.update_compra(compra_id, data)
    
    @staticmethod
    def delete_compra(compra_id):
        return CompraRepository.delete_compra(compra_id)
