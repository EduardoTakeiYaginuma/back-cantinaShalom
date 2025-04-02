# app/Compra/compra_service.py
from app.Compra.compraRepository import CompraRepository
from app.Usuario.usuarioController import UsuarioController
from app.models import Compra
from datetime import date

class CompraService:

    @staticmethod
    def verifica_compra(id_compra):
        compra = CompraRepository.get_compra_by_id(id_compra)
        if not compra:
            raise ValueError("Compra não encontrada")
        return compra
    
    @staticmethod
    def get_all_compras():
        return CompraRepository.get_all_compras()
    
    @staticmethod
    def get_compra_by_id(compra_id):
        return CompraRepository.get_compra_by_id(compra_id)
    
    @staticmethod
    def create_compra(data):
        usuario = UsuarioController.get_usuario(data['usuario_id'])
        if not usuario:
            raise ValueError("Usuário não encontrado")
        
        return CompraRepository.create_compra(data)
    
    @staticmethod
    def update_compra(compra_id, data):
        compra = CompraService.verifica_compra(compra_id)
        return CompraRepository.update_compra(compra, data)
    
    @staticmethod
    def delete_compra(compra_id):
        CompraService.verifica_compra(compra_id)
        return CompraRepository.delete_compra(compra_id)
