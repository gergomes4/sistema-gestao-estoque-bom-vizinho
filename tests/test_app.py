import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config.update({"TESTING": True})

    with app.test_client() as client:
        yield client


def test_pagina_inicial(client):
    resposta = client.get("/")

    assert resposta.status_code == 200
    assert b"Sistema de Gestao de Estoque" in resposta.data
