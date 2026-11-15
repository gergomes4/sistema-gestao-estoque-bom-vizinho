
from flask import Flask, render_template


def create_app():
    """Cria e configura a aplicação Flask."""
    app = Flask(__name__)

    @app.route("/")
    def inicio():
        return "Sistema de Gestão de Estoque - Bom Vizinho"

    @app.route("/produtos")
    def produtos():
        return render_template("produtos.html")

    return app
