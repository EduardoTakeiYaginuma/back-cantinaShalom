from app import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo_usuario = db.Column(db.Integer, nullable=False)
    saldo = db.Column(db.Integer, nullable=True)
    nome = db.Column(db.String(45), nullable=False)
    sobrenome = db.Column(db.String(45), nullable=False)
    nickname = db.Column(db.String(45), nullable=True)
    quarto = db.Column(db.String(45), nullable=False)

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(45), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    tipo = db.Column(db.String(45), nullable=False)
    preco = db.Column(db.Integer, nullable=False)

class Compra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    total = db.Column(db.Integer, nullable=False)
    data = db.Column(db.Date, nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'), nullable=False)
