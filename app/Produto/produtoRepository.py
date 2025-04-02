# app/Produto/produto_repository.py
from app.models import Produto
from app import db

class ProdutoRepository:
    @staticmethod
    def get_all():
        return Produto.query.all()

    @staticmethod
    def get_by_id(produto_id):
        return Produto.query.get(produto_id)

    @staticmethod
    def create(data):
        produto = Produto(
            nome=data['nome'],
            quantidade=data['quantidade'],
            tipo=data['tipo'],
            preco=data['preco']
        )
        db.session.add(produto)
        db.session.commit()
        return produto

    @staticmethod
    def update(produto_id, data):
        produto = Produto.query.get(produto_id)
        if produto:
            produto.nome = data['nome']
            produto.quantidade = data['quantidade']
            produto.tipo = data['tipo']
            produto.preco = data['preco']
            db.session.commit()
        return produto

    @staticmethod
    def delete(produto_id):
        produto = Produto.query.get(produto_id)
        if produto:
            db.session.delete(produto)
            db.session.commit()
