
idades = [39,18,15,27] # Lista
print(idades)
# [39,18,15,27]

print("-----------------------------------------------")

print(28 in idades)
# False

idades.remove(28) if 28 in idades else print("Dado não encontrado")
idades.remove(15) if 15 in idades else print("Dado não encontrado")
print(idades)

print("-----------------------------------------------")

idades.insert(0, 99) #inserir no início da lista
print(idades)

idades.insert(len(idades), 98) #inserir no final
print(idades)

print("-----------------------------------------------")

# idades.append(27, 19) #Error
idades.append([27, 19])
print(idades)

for elemento in idades:
    print(f"Incluído o seguinte elemento: {elemento}")

print("-----------------------------------------------")

print(idades)

# idades.remove('[27, 19]') # Error
idades.remove([27, 19])
# idades.remove(idades[5])
print(idades)

idades.extend([27, 19])
print(idades)

print("-----------------------------------------------")

# del idades[:] # Deletar tudo
# idades.clear() # Deletar tudo
del idades[0:1]
print(idades)

del idades[3:]
print(idades)

print("-----------------------------------------------")

idades.insert(0, 20)
idades.insert(len(idades), 19)
print(idades)

print("-----------------------------------------------")

idades_no_ano_que_vem = []
for idade in idades:
  idades_no_ano_que_vem.append(idade+1)

print(idades_no_ano_que_vem)

# ou

idades_no_ano_que_vem = [(idade + 1) for idade in idades]
print(idades_no_ano_que_vem)

print("-----------------------------------------------")

print([(idade) for idade in idades if idade > 21])

print("-----------------------------------------------")

def proximo_ano(idade):
    return (idade + 1)

print([proximo_ano(idade) for idade in idades if idade > 21])