import pytest

from app import create_app
from app.store import reset_produtos


@pytest.fixture
def client():
    reset_produtos()

    app = create_app(testing=True)

    with app.test_client() as test_client:
        yield test_client

    reset_produtos()


@pytest.fixture
def produto_valido():
    return {
        "nome": "Pulseira Riviera",
        "categoria": "pulseira",
        "material": "banhado a ouro 18k",
        "preco": 129.90,
        "estoque": 8,
        "ativo": True,
    }
