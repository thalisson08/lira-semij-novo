def test_listar_produtos_retorna_200(client):
    resposta = client.get("/produtos")

    assert resposta.status_code == 200


def test_listar_produtos_retorna_lista(client):
    resposta = client.get("/produtos")
    dados = resposta.get_json()

    assert isinstance(dados, list)
    assert len(dados) == 2


def test_listar_produtos_filtra_por_categoria(client):
    resposta = client.get("/produtos?categoria=colar")
    dados = resposta.get_json()

    assert resposta.status_code == 200
    assert len(dados) == 1
    assert dados[0]["categoria"] == "colar"
