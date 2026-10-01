def test_obter_produto_existente(client):
    resposta = client.get("/produtos/1")
    dados = resposta.get_json()

    assert resposta.status_code == 200
    assert dados["id"] == 1


def test_obter_produto_retorna_campos_esperados(client):
    resposta = client.get("/produtos/1")
    dados = resposta.get_json()

    assert dados["nome"] == "Colar Ponto de Luz"
    assert dados["preco"] == 89.90
    assert dados["estoque"] == 10


def test_obter_produto_inexistente_retorna_404(client):
    resposta = client.get("/produtos/999")
    dados = resposta.get_json()

    assert resposta.status_code == 404
    assert dados["erro"] == "Produto não encontrado."
