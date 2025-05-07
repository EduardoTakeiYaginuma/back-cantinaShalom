from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
import os
from flask_cors import CORS





load_dotenv()  
app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# app/__init__.py
from app.Usuario.usuarioRoutes import usuario_bp
app.register_blueprint(usuario_bp)

from app.Produto.produtoRoutes import produto_bp
app.register_blueprint(produto_bp)

from app.Compra.compraRoutes import compra_bp
app.register_blueprint(compra_bp)

from app.Compra_Produto.compraProdutoRoutes import compraProduto_bp
app.register_blueprint(compraProduto_bp)

