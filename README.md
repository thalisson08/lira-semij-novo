# Lira Semijoias API

API REST desenvolvida em Python para representar o catálogo de produtos da
**Lira Semijoias**.

O projeto foi criado para a Fase 1 da disciplina, com foco em versionamento,
testes automatizados, lint e integração contínua usando GitLab CI.

## Funcionalidades

A API permite:

verificar se a aplicação está funcionando;
 listar produtos;
 filtrar produtos por categoria;
 buscar um produto por ID;
 cadastrar um novo produto;
 atualizar um produto;
 remover um produto.

## Tecnologias utilizadas

 Python 3.12
 Flask
 Pytest
 Flake8
 Git
 GitLab
 GitLab CI/CD
## Rotas

 Método  Rota  Descrição 

 GET  `/health`  Healthcheck da aplicação 
 GET  `/produtos`  Lista todos os produtos
 GET `/produtos?categoria=colar`  Filtra produtos por categoria 
 GET  `/produtos/<id>`  Busca um produto pelo ID 
 POST  `/produtos`  Cadastra um produto 
 PUT `/produtos/<id>`  Atualiza um produto 
 DELETE  `/produtos/<id>`  Exclui um produto 

 Como rodar o projeto localmente

 Criar um ambiente virtual

```bash
python -m venv .venv
.venv\Scripts\activate
```



```bash
python3 -m venv .venv
source .venv/bin/activate
```

 Instalar as dependências

```bash
pip install -r requirements-dev.txt
```

### 4. Executar a aplicação

```bash
python run.py
```

A API ficará disponível em:

```text
http://localhost:5000
```

## Exemplo de cadastro

Requisição:

```http
POST /produtos
Content-Type: application/json
```

JSON:

```json
{
  "nome": "Pulseira Riviera",
  "categoria": "pulseira",
  "material": "banhado a ouro 18k",
  "preco": 129.90,
  "estoque": 8,
  "ativo": true
}
```

## Executar os testes

```bash
python -m pytest -v
```

O projeto possui **18 testes automatizados**, cobrindo:

 respostas de sucesso;
 validações de dados;
 recursos inexistentes;
 criação de produtos;
 atualização de produtos;
-remoção de produtos;


## Executar o lint

```bash
flake8 app tests run.py
```

Estratégia de branches

O projeto deve utilizar pelo menos:

`main`: branch principal e estável;
`develop`: branch de desenvolvimento.



/health
produtos

http://localhost:5000/produtos
http://localhost:5000/health