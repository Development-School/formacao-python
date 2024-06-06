print("-----------------------------------------------")

lista = {
    'chocolate' : 3.45,
    'biscoito' : 2.49,
    'cafe' : 3.45,
    'suco' : 4.3,
    'feijao' : 10.0,
    'arroz' : 8.5
}

for nome, valor in lista.items():
    print(nome, valor)

# chocolate 3.45
# biscoito 2.49
# cafe 3.45
# suco 4.3
# feijao 10.0
# arroz 8.5

print("-----------------------------------------------")

numeros = [4,2,6,1,3]
numeros_ordenados = sorted(numeros)

print(numeros)
print(numeros_ordenados)
# [4, 2, 6, 1, 3]
# [1, 2, 3, 4, 6]

print("-----------------------------------------------")


palavras = ["chocolate","biscoito", "cafe", "suco", "feijao", "arroz"]
palavras_ordenadas = sorted(palavras)

print(palavras)
print(palavras_ordenadas)
# ['chocolate', 'biscoito', 'cafe', 'suco', 'feijao', 'arroz']
# ['arroz', 'biscoito', 'cafe', 'chocolate', 'feijao', 'suco']

print("-----------------------------------------------")

a = [5, 2, 3, 1, 4]
a.sort()
print(a)
# [1, 2, 3, 4, 5]

print("-----------------------------------------------")

b = {1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}
print(b)
# {1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}
print(type(b))
# <class 'dict'>
print()

from operator import itemgetter

b = dict(sorted(b.items(), key=itemgetter(1)))
print(b)
# {5: 'A', 2: 'B', 3: 'B', 1: 'D', 4: 'E'}
print(type(b))
# <class 'dict'>

print("-----------------------------------------------")

print(lista)
# {'chocolate': 3.45, 'biscoito': 2.49, 'cafe': 3.45, 'suco': 4.3, 'feijao': 10.0, 'arroz': 8.5}

print("-----------------------------------------------")

produtos = lista
print(produtos)
# {'chocolate': 3.45, 'biscoito': 2.49, 'cafe': 3.45, 'suco': 4.3, 'feijao': 10.0, 'arroz': 8.5}
print(type(produtos))
# <class 'dict'>

print("-----------------------------------------------")


produtos_ordenados = sorted(produtos, key=lambda item:item[0])
print(produtos_ordenados)
# ['arroz', 'biscoito', 'chocolate', 'cafe', 'feijao', 'suco']
print(type(produtos_ordenados))
# <class 'list'>

print("-----------------------------------------------")

print(produtos)
# {'chocolate': 3.45, 'biscoito': 2.49, 'cafe': 3.45, 'suco': 4.3, 'feijao': 10.0, 'arroz': 8.5}

produtos_ordenados = dict(sorted(produtos.items(), key=lambda item: item[0]))
print(produtos_ordenados)
# {'arroz': 8.5, 'biscoito': 2.49, 'cafe': 3.45, 'chocolate': 3.45, 'feijao': 10.0, 'suco': 4.3}

print("-----------------------------------------------")