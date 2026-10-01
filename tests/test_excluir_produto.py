def test_excluir_produto_existente(client):
    resposta = client.delete("/produtos/1")
    dados = resposta.get_json()

    assert resposta.status_code == 200
    assert dados["mensagem"] == "Produto removido com sucesso."


def test_excluir_produto_remove_da_listagem(client):
    client.delete("/produtos/1")

    resposta = client.get("/produtos/1")

    assert resposta.status_code == 404


def test_excluir_produto_inexistente_retorna_404(client):
    resposta = client.delete("/produtos/999")
    dados = resposta.get_json()

    assert resposta.status_code == 404
    assert dados["erro"] == "Produto não encontrado."
