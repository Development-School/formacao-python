
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

print(carne_assada.__dict__)
# {'_nome': 'Carne assada', '_preco': 5.0, 'descricao': 'Carne assada na panela de pressão', 'tipo': '', 'tamanho': ''}

print("-----------------------------------------------")

print('Trabalhando com in ... Objeto')
print('descricao' in dir(Prato)) # False
print('descricao' in dir(carne_assada)) # True

print("-----------------------------------------------")

print('x, y, e z in ... Objeto')
x = [1, 2, 3]
print(1 in x) # True
print((1 and 2 and 3) in x) # True

print("-----------------------------------------------")

print(f"'descricao' and 'tipo' and 'tamanho' in carne_assada...")
print(('descricao' and 'tipo' and 'tamanho') in dir(carne_assada)) # True

print("-----------------------------------------------")

# Saber o nome de uma classe: ▼
print(Prato.__name__) # Prato

# Saber o nome de uma instancia de uma classe: ▼
# print(carne_assada.__name__) # Error
print(carne_assada.__class__.__name__) # Prato
print(type(carne_assada).__name__) # Prato

print("-----------------------------------------------")
