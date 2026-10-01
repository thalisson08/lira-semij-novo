def test_healthcheck_retorna_200(client):
    resposta = client.get("/health")

    assert resposta.status_code == 200


def test_healthcheck_retorna_status_ok(client):
    resposta = client.get("/health")
    dados = resposta.get_json()

    assert dados["status"] == "ok"


def test_healthcheck_identifica_aplicacao(client):
    resposta = client.get("/health")
    dados = resposta.get_json()

    assert dados["aplicacao"] == "Lira Semijoias API"
