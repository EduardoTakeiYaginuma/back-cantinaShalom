from flask import request, jsonify
from app import app, db
from app.models import Usuario, Produto, Compra

@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([{'id': u.id, 'nome': u.nome, 'sobrenome': u.sobrenome, 'saldo': u.saldo} for u in usuarios])

@app.route('/produtos', methods=['GET'])
def get_produtos():
    produtos = Produto.query.all()
    return jsonify([{'id': p.id, 'nome': p.nome, 'quantidade': p.quantidade, 'preco': p.preco} for p in produtos])

@app.route('/compras', methods=['POST'])
def criar_compra():
    data = request.json
    nova_compra = Compra(total=data['total'], data=data['data'], usuario_id=data['usuario_id'], produto_id=data['produto_id'])
    db.session.add(nova_compra)
    db.session.commit()
    return jsonify({'message': 'Compra registrada com sucesso!'}), 201
