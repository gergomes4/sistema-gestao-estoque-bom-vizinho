from flask import Flask


def create_app():
    """Cria e configura a aplicação Flask."""
    app = Flask(__name__)

    @app.route("/")
    def inicio():
        return "Sistema de Gestão de Estoque - Bom Vizinho"

    return app
