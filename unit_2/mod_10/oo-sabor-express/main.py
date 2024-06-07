
from modelos.restaurante import Restaurante

restaurante_praca = Restaurante()
restaurante_pizza = Restaurante()

restaurantes = [restaurante_praca, restaurante_pizza]

print(restaurantes)
# [<modelos.restaurante.Restaurante object at 0x0000022F8DE44320>, <modelos.restaurante.Restaurante object at 0x0000022F8DE442F0>]

print("-----------------------------------------------")

restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

print(restaurante_praca)
# <modelos.restaurante.Restaurante object at 0x0000022F8DE44320>

print("-----------------------------------------------")

print(dir(restaurante_praca))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__'
# , '__eq__', '__format__', '__ge__', '__getattribute__'
# , '__getstate__', '__gt__', '__hash__', '__init__'
# , '__init_subclass__', '__le__', '__lt__', '__module__'
# , '__ne__', '__new__', '__reduce__', '__reduce_ex__'
# , '__repr__', '__setattr__', '__sizeof__', '__str__'
# , '__subclasshook__', '__weakref__', 'ativo', 'categoria'
# , 'nome']

print("-----------------------------------------------")

print(vars(restaurante_praca))
# {'nome': 'Praça', 'categoria': 'Gourmet'}

print("-----------------------------------------------")

# ...

print("-----------------------------------------------")