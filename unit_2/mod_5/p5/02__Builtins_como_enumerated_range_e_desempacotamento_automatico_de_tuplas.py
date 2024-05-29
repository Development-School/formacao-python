
idades = [15, 87, 65, 56, 32, 49, 37]

for idade in idades:
  print(idade)

# 15
# 87
# 65
# 56
# 32
# 49
# 37

print("-----------------------------------------------")

idades = [15, 87, 32, 65, 56, 32, 49, 37]

print(range(len(idades)))
# range(0, 8)

print("-----------------------------------------------")

idades = [15, 87, 32, 65, 56, 32, 49, 37]

for i in range(len(idades)):
  print(i, idades[i])

# 0 15
# 1 87
# 2 32
# 3 65
# 4 56
# 5 32
# 6 49
# 7 37

print("-----------------------------------------------")

print(range(len(idades))) # lazy (ocioso)...
# range(0, 8)
print(enumerate(idades))  # lazy...
# <enumerate object at 0x000001AF1A0BD6C0>

print("-----------------------------------------------")

# Forcei a geração dos valores
print(list(range(len(idades))))
print(list(enumerate(idades)))

print("-----------------------------------------------")

for valor in enumerate(idades):
  print(valor)

# (0, 15)
# (1, 87)
# (2, 32)
# (3, 65)
# (4, 56)
# (5, 32)
# (6, 49)
# (7, 37)

print("-----------------------------------------------")

for indice, idade in enumerate(idades):
  print(indice, idade)

# 0 15
# 1 87
# 2 32
# 3 65
# 4 56
# 5 32
# 6 49
# 7 37

print("-----------------------------------------------")

for indice, idade in enumerate(idades): # unpacking da nossa tupla
  print(indice, "x", idade)

# 0 x 15
# 1 x 87
# 2 x 32
# 3 x 65
# 4 x 56
# 5 x 32
# 6 x 49
# 7 x 37

print("-----------------------------------------------")

usuarios = [
    ("Guilherme", 37, 1981),
    ("Daniela", 31, 1987),
    ("Paulo", 39, 1979)
]

for usuario in usuarios: # Empacotado
  print(usuario)

print("-----------------------------------------------")

for nome, idade, nascimento in usuarios: # ja desempacotando
  print(nome)
  # print(f'Nome: {nome}, idade: {idade}, Data de nascimento: {nascimento}')

# Guilherme
# Daniela
# Paulo

print("---Ou---") # Ou

for usuario in usuarios:
    print(usuario[0])

print("-----------------------------------------------")

for nome, _, _ in usuarios: # ja desempacotando, ignorando o resto
  print(nome)

# Guilherme
# Daniela
# Paulo

print("-----------------------------------------------")

for nome, *_ in usuarios: # ja desempacotando, ignorando o resto
    print(nome)

# Guilherme
# Daniela
# Paulo

print("-----------------------------------------------")

for *_, ultimo in usuarios: # ja desempacotando, ignorando o resto porém pegando o último
    print(ultimo)

# 1981
# 1987
# 1979

print("-----------------------------------------------")

for primeiro, *_ in usuarios:  # ja desempacotando, ignorando o resto porém pegando o primeiro
  print(primeiro)

# Guilherme
# Daniela
# Paulo

print("-----------------------------------------------")

# for *_, meio, *_ in usuarios:  # ja desempacotando, ignorando o resto porém pegando o primeiro
#   print(meio) # ERROR não funciona para pegar os do meio kkkk