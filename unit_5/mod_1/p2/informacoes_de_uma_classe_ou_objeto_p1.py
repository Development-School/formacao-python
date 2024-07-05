
class ItemCardapio():
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao="", tipo="", tamanho=""):
        super().__init__ (nome, preco) # Herança da classe Mãe
        self.descricao = descricao
        self.tipo = tipo
        self.tamanho = tamanho

    def __str__(self):
        return self._nome

print("-----------------------------------------------")

carne_assada = Prato('Carne assada', 5.00, 'Carne assada na panela de pressão')
print(carne_assada)

print("-----------------------------------------------")

# Verificar se é uma instancia da ItemCardapio: ▼
# "carne_assada" é uma instancia da Classe "Prato"??
print('verificar com isinstance()')
print(isinstance(carne_assada, Prato)) # True

# "carne_assada" é uma instancia da Classe "ItemCardapio"??
# Ela é filha pois herda da mãe atributos e métodos...
print(isinstance(carne_assada, ItemCardapio)) # True

print("-----------------------------------------------")

# Verificar se a instancia tem um atributo XPTO: ▼
# "carne_assada" possui algum atributo com o nome "descricao"??
print('verificar com hasattr()')
print(hasattr(carne_assada, 'descricao')) # True

print("-----------------------------------------------")

# "carne_assada" possui algum atributo com o nome "preco"??
print('verificar com hasattr()')
print(
    hasattr(carne_assada, 'nome') and
    hasattr(carne_assada, 'preco')
) # False
# pois ela não tem esses atributos diretamente e sim
# atributos herdados...

print("-----------------------------------------------")

# "carne_assada" possui algum desses atributos?
print('verificar com hasattr()')
print(
    hasattr(carne_assada, 'descricao') or
    hasattr(carne_assada, 'preco')
) # True

print("-----------------------------------------------")

# Ver diretórios de um objeto: ▼
print('dir(Prato)')
print(dir(Prato))
r"""
['__abstractmethods__', '__class__', '__delattr__', 
'__dict__', '__dir__', '__doc__', '__eq__', '__format__',
'__ge__', '__getattribute__', '__getstate__', '__gt__', 
'__hash__', '__init__', '__init_subclass__', '__le__',
'__lt__', '__module__', '__ne__', '__new__', '__reduce__', 
'__reduce_ex__', '__repr__', '__setattr__','__sizeof__', 
'__slots__', '__str__', '__subclasshook__', '__weakref__', 
'_abc_impl', 'aplicar_desconto']
"""

print()

print('dir(carne_assada)')
print(dir(carne_assada))
r"""
['__class__', '__delattr__', '__dict__', '__dir__', 
'__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__getstate__', '__gt__', '__hash__', 
'__init__', '__init_subclass__', '__le__', '__lt__', 
'__module__', '__ne__', '__new__', '__reduce__', 
'__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
'__str__', '__subclasshook__', '__weakref__', '_nome', 
'_preco', 'descricao', 'tamanho', 'tipo']
"""

print("-----------------------------------------------")

# Ver variáveis de um objeto
print('vars(Prato)')
"""
{'__module__': '__main__', 
'__init__': <function Prato.__init__ at 0x000002221C558180>, 
'__str__': <function Prato.__str__ at 0x000002221C5596C0>, 
'__doc__': None}
"""
print(vars(Prato))

print()

print('vars(carne_assada)')
print(vars(carne_assada))
r"""
{'_nome': 'Carne assada', '_preco': 5.0, 
'descricao': 'Carne assada na panela de pressão', 
'tipo': '', 'tamanho': ''}
"""

print("-----------------------------------------------")

# Outros: ▼
print(Prato.__getattribute__)
print(hash(Prato))
print(Prato.__dir__)

print("-----------------------------------------------")

# Ver um resumo da classe
print(help(Prato))
r"""
Help on class Prato in module __main__:

class Prato(builtins.object)
 |  Prato(nome, preco, descricao)
 |
 |  Methods defined here:
 |
 |  __init__(self, nome, preco, descricao)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables
 |
 |  __weakref__
 |      list of weak references to the object

None
-----------------------------------------------

Process finished with exit code 0
"""

print("-----------------------------------------------")
