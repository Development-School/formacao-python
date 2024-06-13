
# from atividade_pratica import Livro
from minha_classe import *

# 6) No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o
# livro está disponível ou não após o empréstimo.

main()

print("-----------------------------------------------")

livro_biblioteca = Livro("Python in Practice", "Emily Coder", 2021)
print(f"Antes de emprestar (biblioteca): Livro disponível? {livro_biblioteca.disponivel}")

livro_biblioteca.emprestar()
print(f"Depois de emprestar (biblioteca): Livro disponível? {livro_biblioteca.disponivel}")

print("-----------------------------------------------")

# 7) No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter
# a lista de livros disponíveis publicados em um ano específico.
ano_especifico = 2020
livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_especifico)
print(f"Livros disponíveis em {ano_especifico}: {livros_disponiveis_ano}")
# Livros disponíveis em 2020: [<minha_classe.Livro object at 0x000002CE448C7A10>]

print()

print(f"Livros disponíveis em {ano_especifico}:")
for livros in livros_disponiveis_ano:
    print(livros)

print("-----------------------------------------------")

# 8) Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois
# objetos da classe Livro e exiba a mensagem formatada utilizando o método __str__.

# ... Continuação no arquivo main.py...