def test_criar_produto_valido(client, produto_valido):
    resposta = client.post("/produtos", json=produto_valido)
    dados = resposta.get_json()

    assert resposta.status_code == 201
    assert dados["nome"] == "Pulseira Riviera"
    assert dados["id"] == 3


def test_criar_produto_aumenta_quantidade(client, produto_valido):
    client.post("/produtos", json=produto_valido)

    resposta = client.get("/produtos")
    dados = resposta.get_json()

    assert len(dados) == 3


def test_criar_produto_invalido_retorna_400(client):
    produto_invalido = {
        "nome": "Anel Solitário",
        "categoria": "anel",
        "material": "banhado a ouro 18k",
        "estoque": 4,
    }

    resposta = client.post("/produtos", json=produto_invalido)
    dados = resposta.get_json()

    assert resposta.status_code == 400
    assert "preco" in dados["erro"]
