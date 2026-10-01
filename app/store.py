PRODUTOS_INICIAIS = [
    {
        "id": 1,
        "nome": "Colar Ponto de Luz",
        "categoria": "colar",
        "material": "banhado a ouro 18k",
        "preco": 89.90,
        "estoque": 10,
        "ativo": True,
    },
    {
        "id": 2,
        "nome": "Brinco Argola Elegance",
        "categoria": "brinco",
        "material": "banhado a ouro 18k",
        "preco": 69.90,
        "estoque": 15,
        "ativo": True,
    },
]


produtos = []


def reset_produtos():
    produtos.clear()
    for produto in PRODUTOS_INICIAIS:
        produtos.append(produto.copy())


def proximo_id():
    if not produtos:
        return 1
    return max(produto["id"] for produto in produtos) + 1


reset_produtos()
