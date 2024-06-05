print("-----------------------------------------------")

aparicoes = {
  # Chave : Valor
  "Guilherme" : 1,
  "cachorro" : 2,
  "nome" : 2,
  "vindo" : 1
}

print(aparicoes)

print("-----------------------------------------------")

aparicoes["Carlos"] = 1
print(aparicoes)
# {'Guilherme': 1, 'cachorro': 2, 'nome': 2, 'vindo': 1, 'Carlos': 1}

aparicoes["Carlos"] = 2
print(aparicoes)
# {'Guilherme': 1, 'cachorro': 2, 'nome': 2, 'vindo': 1, 'Carlos': 2}

print("-----------------------------------------------")

del aparicoes["Carlos"]
print(aparicoes)
# {'Guilherme': 1, 'cachorro': 2, 'nome': 2, 'vindo': 1}

print("-----------------------------------------------")

print("cachorro" in aparicoes)
# True
print("Carlos" in aparicoes)
# False

print("-----------------------------------------------")

for elemento in aparicoes:
  print(elemento)

# Guilherme
# cachorro
# nome
# vindo

print("-----------------------------------------------")

# for elemento in aparicoes.iterkeys(): #Error
for elemento in aparicoes.keys():
  print(elemento)

# Guilherme
# cachorro
# nome
# vindo

print("-----------------------------------------------")

for elemento in aparicoes.values():
  print(elemento)

# 1
# 2
# 2
# 1

print("-----------------------------------------------")

print(1 in aparicoes.values())
# True

print("-----------------------------------------------")

for elemento in aparicoes.keys():
  print(elemento, ":", aparicoes[elemento])

# Guilherme : 1
# cachorro : 2
# nome : 2
# vindo : 1

print("-----------------------------------------------")

for elemento in aparicoes.items():
  print(elemento)

# ('Guilherme', 1)
# ('cachorro', 2)
# ('nome', 2)
# ('vindo', 1)

print("-----------------------------------------------")

for chave, valor in aparicoes.items():
  print(chave, "=", valor)

# Guilherme = 1
# cachorro = 2
# nome = 2
# vindo = 1

print("-----------------------------------------------")

print(["palavra {}".format(chave) for chave in aparicoes.keys()])

# ['palavra Guilherme', 'palavra cachorro', 'palavra nome', 'palavra vindo']

print("-----------------------------------------------")