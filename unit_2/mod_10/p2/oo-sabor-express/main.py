
from modelos.restaurante import Restaurante

print("-----------------------------------------------")

# restaurante_praca.nome = 'Praça'
# restaurante_praca.categoria = 'Gourmet'

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

restaurantes = [vars(restaurante_praca), vars(restaurante_pizza)]

print(restaurantes)
# [{'nome': 'Praça', 'categoria': 'Gourmet', 'status': False}, {'nome': 'Pizza Express', 'categoria': 'Italiana', 'status': False}]

print("-----------------------------------------------")

print(restaurante_praca)
print(restaurante_pizza)
# Praça | Gourmet
# Pizza Express | Italiana

print("-----------------------------------------------")

Restaurante.listar_restaurantes()

print("-----------------------------------------------")

# ...

print("-----------------------------------------------")

# ...

print("-----------------------------------------------")