# Biblioteca Digital
Projeto acadêmico demonstrativo de Gerência de Configuração - UFRPE.

## Objetivo
Organizar um catálogo de livros e permitir consultas simples.

## Funcionalidades
- Cadastro de livros com título e autor;
- Consulta de livros;
- Validação de campos obrigatórios;
- Busca por título ou autor (a partir de v1.1.0).

## Integrante
Mateus Teixeira da Silva. Implementação preparada com auxílio de IA.

## Execução
Python 3.10 ou superior, sem dependências externas.
```bash
python -m src.app
python -m unittest discover -s tests -v
```
Os dados permanecem em memória durante a execução; não há autenticação nem banco de dados.

## Versões
v1.0.0: cadastro, busca por título e validação.
v1.1.0: busca ampliada para título ou autor.

## Histórico
```bash
git log --oneline --decorate --all
git show v1.0.0
git diff v1.0.0 v1.1.0 -- src/biblioteca.py
```
