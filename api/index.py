"""Entrypoint serverless da Vercel.

A Vercel procura um objeto WSGI chamado `app` dentro de `api/`.
Todas as rotas são redirecionadas para cá via `vercel.json`.
"""
import os
import sys

# Garante que o pacote `app` (na raiz do projeto) seja encontrado.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app  # noqa: E402

app = create_app()
