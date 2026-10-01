def test_atualizar_preco_produto(client):
    resposta = client.put("/produtos/1", json={"preco": 99.90})
    dados = resposta.get_json()

    assert resposta.status_code == 200
    assert dados["preco"] == 99.90


def test_atualizar_produto_inexistente_retorna_404(client):
    resposta = client.put("/produtos/999", json={"preco": 99.90})
    dados = resposta.get_json()

    assert resposta.status_code == 404
    assert dados["erro"] == "Produto não encontrado."


def test_atualizar_com_dado_invalido_retorna_400(client):
    resposta = client.put("/produtos/1", json={"estoque": -1})
    dados = resposta.get_json()

    assert resposta.status_code == 400
    assert "estoque" in dados["erro"]
