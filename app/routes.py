from flask import Blueprint, jsonify, request

from app.store import produtos, proximo_id


api = Blueprint("api", __name__)


def buscar_produto(produto_id):
    return next(
        (
            produto
            for produto in produtos
            if produto["id"] == produto_id
        ),
        None,
    )


def validar_produto(dados, parcial=False):
    campos_obrigatorios = {
        "nome",
        "categoria",
        "material",
        "preco",
        "estoque",
    }

    if not isinstance(dados, dict):
        return "O corpo da requisição deve ser um JSON válido."

    if not parcial:
        faltando = campos_obrigatorios - dados.keys()
        if faltando:
            campos = ", ".join(sorted(faltando))
            return f"Campos obrigatórios ausentes: {campos}."

    if "nome" in dados:
        if not isinstance(dados["nome"], str) or not dados["nome"].strip():
            return "O campo 'nome' deve ser um texto não vazio."

    if "categoria" in dados:
        if (
            not isinstance(dados["categoria"], str)
            or not dados["categoria"].strip()
        ):
            return "O campo 'categoria' deve ser um texto não vazio."

    if "material" in dados:
        if (
            not isinstance(dados["material"], str)
            or not dados["material"].strip()
        ):
            return "O campo 'material' deve ser um texto não vazio."

    if "preco" in dados:
        if (
            isinstance(dados["preco"], bool)
            or not isinstance(dados["preco"], (int, float))
            or dados["preco"] <= 0
        ):
            return "O campo 'preco' deve ser maior que zero."

    if "estoque" in dados:
        if (
            isinstance(dados["estoque"], bool)
            or not isinstance(dados["estoque"], int)
            or dados["estoque"] < 0
        ):
            return "O campo 'estoque' deve ser um inteiro maior ou igual a zero."

    if "ativo" in dados and not isinstance(dados["ativo"], bool):
        return "O campo 'ativo' deve ser booleano."

    return None


@api.get("/health")
def healthcheck():
    return jsonify(
        {
            "status": "ok",
            "aplicacao": "Lira Semijoias API",
        }
    ), 200


@api.get("/produtos")
def listar_produtos():
    categoria = request.args.get("categoria")

    if categoria:
        resultado = [
            produto
            for produto in produtos
            if produto["categoria"].lower() == categoria.lower()
        ]
    else:
        resultado = produtos

    return jsonify(resultado), 200


@api.get("/produtos/<int:produto_id>")
def obter_produto(produto_id):
    produto = buscar_produto(produto_id)

    if produto is None:
        return jsonify({"erro": "Produto não encontrado."}), 404

    return jsonify(produto), 200


@api.post("/produtos")
def criar_produto():
    dados = request.get_json(silent=True)
    erro = validar_produto(dados)

    if erro:
        return jsonify({"erro": erro}), 400

    novo_produto = {
        "id": proximo_id(),
        "nome": dados["nome"].strip(),
        "categoria": dados["categoria"].strip(),
        "material": dados["material"].strip(),
        "preco": float(dados["preco"]),
        "estoque": dados["estoque"],
        "ativo": dados.get("ativo", True),
    }

    produtos.append(novo_produto)

    return jsonify(novo_produto), 201


@api.put("/produtos/<int:produto_id>")
def atualizar_produto(produto_id):
    produto = buscar_produto(produto_id)

    if produto is None:
        return jsonify({"erro": "Produto não encontrado."}), 404

    dados = request.get_json(silent=True)

    if not dados:
        return jsonify({"erro": "Envie ao menos um campo para atualizar."}), 400

    erro = validar_produto(dados, parcial=True)
    if erro:
        return jsonify({"erro": erro}), 400

    campos_editaveis = {
        "nome",
        "categoria",
        "material",
        "preco",
        "estoque",
        "ativo",
    }

    for campo in campos_editaveis:
        if campo in dados:
            valor = dados[campo]
            if isinstance(valor, str):
                valor = valor.strip()
            if campo == "preco":
                valor = float(valor)
            produto[campo] = valor

    return jsonify(produto), 200


@api.delete("/produtos/<int:produto_id>")
def excluir_produto(produto_id):
    produto = buscar_produto(produto_id)

    if produto is None:
        return jsonify({"erro": "Produto não encontrado."}), 404

    produtos.remove(produto)

    return jsonify(
        {
            "mensagem": "Produto removido com sucesso.",
            "produto": produto,
        }
    ), 200
