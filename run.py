from app import app, db
from app.models import Usuario, Produto, Compra, CompraProduto
import os

def setup_database():
    try:
        with app.app_context():
            db.drop_all()
            db.create_all()

            if not Usuario.query.first():
                usuario1 = Usuario(tipo_usuario=1, saldo=100, nome="João", sobrenome="Silva", quarto="101")
                usuario2 = Usuario(tipo_usuario=2, saldo=50, nome="Maria", sobrenome="Oliveira", quarto="102")
                usuario3 = Usuario(tipo_usuario=1, saldo=200, nome="Carlos", sobrenome="Pereira", quarto="103")
                usuario4 = Usuario(tipo_usuario=3, saldo=150, nome="Ana", sobrenome="Souza", quarto="104")
                db.session.add(usuario3)
                db.session.add(usuario4)
                db.session.add(usuario1)
                db.session.add(usuario2)
                db.session.commit()

            if not Produto.query.first():
                produto1 = Produto(nome="Cachorro Quente", quantidade=50, tipo="Doce", preco=10)
                produto2 = Produto(nome="Refrigerante", quantidade=30, tipo="Bebida", preco=5)
                produto3 = Produto(nome="Pizza", quantidade=20, tipo="Salgadinho", preco=20)
                produto4 = Produto(nome="Água", quantidade=100, tipo="Bebida", preco=2)
                db.session.add(produto1)
                db.session.add(produto2)
                db.session.add(produto3)
                db.session.add(produto4)
                db.session.commit()

            if not Compra.query.first():
                compra1 = Compra(total=15, data="2023-10-01", usuario_id=1)
                compra2 = Compra(total=5, data="2023-10-02", usuario_id=2)
                db.session.add(compra1)
                db.session.add(compra2)
                db.session.commit()

                # Adicionando produtos às compras na tabela CompraProduto
                compra_produto1 = CompraProduto(compra_id=compra1.id, produto_id=1, quantidade=1)
                compra_produto2 = CompraProduto(compra_id=compra1.id, produto_id=2, quantidade=1)
                compra_produto3 = CompraProduto(compra_id=compra2.id, produto_id=2, quantidade=1)
                db.session.add(compra_produto1)
                db.session.add(compra_produto2)
                db.session.add(compra_produto3)
                db.session.commit()
    except Exception as e:
        print(f"Erro ao configurar o banco de dados: {e}")

if __name__ == '__main__':
    setup_database()
    app.run(host='0.0.0.0', port=8080)