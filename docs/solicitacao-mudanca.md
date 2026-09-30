# SM-001 - Busca por autor
Registro anterior à implementação.

O que será modificado: ampliar a consulta para pesquisar título OU autor,
preservando a busca sem distinção de maiúsculas/minúsculas e o tratamento de espaços.
Motivo: o usuário pode conhecer o autor e não recordar o título da obra.
Arquivos afetados: src/biblioteca.py e tests/test_biblioteca.py.
Critérios de aceitação: encontrar por autor, manter busca por título e retornar
lista vazia quando não houver correspondência.
Baseline: v1.0.0. A alteração não modifica os dados cadastrados.
