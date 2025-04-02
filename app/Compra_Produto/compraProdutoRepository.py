from app import db
from app.models import CompraProduto


class CompraProdutoRepository:
    
    @staticmethod
    def get_all():
        return CompraProduto.query.all()

    @staticmethod
    def get_by_id(compraProduto_id):
        return CompraProduto.query.get(compraProduto_id)

    @staticmethod
    def create(compraProduto):
        db.session.add(compraProduto)
        db.session.commit()
        return compraProduto

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(compraProduto):
        db.session.delete(compraProduto)
        db.session.commit()