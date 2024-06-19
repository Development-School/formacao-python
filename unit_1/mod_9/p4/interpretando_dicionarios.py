# -------------------------------------------------------------------- #
# 06. Interpretando dicionários
# -------------------------------------------------------------------- #


livro = {
    'titulo': 'Aprendendo Python',
    'autor': 'Fabrício Silva',
    'ISBN': '12345',
    'preco': 59.90,
    'em_estoque': True
}

print(livro['preco']) # 59.9

livro.update({'preco': 70.90})

print(livro['preco']) # 70.9