
# Continuando com Collections

usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

teste = []
teste.extend(usuarios_data_science)
print(list(teste))
# [15, 23, 43, 56]

print("-----------------------------------------------")

assistiram = usuarios_data_science.copy()
print(assistiram)

print("-----------------------------------------------")

assistiram.extend(usuarios_machine_learning)
print(assistiram)

print("-----------------------------------------------")

print(type(assistiram))
# <class 'list'>

# Transformar uma lista em um conjunto... Isso fará com que os elementos repetidos sejam ignorados
print(type(set(assistiram)))
# <class 'set'>

print("---")

# set(assistiram) # Comando não funcionou!!
set(assistiram) # Dessa forma ele não converte para set, # Ainda acusando como List
print(type(assistiram))
# <class 'list'>
print(assistiram)

print("---")

assistiram = set(assistiram) # Dessa forma funciona
print(type(assistiram))
print(assistiram)

print("-----------------------------------------------")

# Outra forma (revertendo para lista sem as duplicações):
assistiram = list(dict.fromkeys(assistiram))
print(type(assistiram))
print(assistiram)

print("-----------------------------------------------")

print(set([1,2,3,1]))
# {1, 2, 3}

print("-----------------------------------------------")

# ATENÇÃO!! Em conjuntos não existem acesso a índex dos elementos, diferentes das listas
print(list([1,2,3,1])[0])
# 1
# print(set([1,2,3,1])[0]) # Error
# TypeError: 'set' object is not subscriptable

print("-----------------------------------------------")

usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

usuarios = usuarios_data_science.copy()
usuarios.update(usuarios_machine_learning) # Adidionar set a usuarios

print(type(usuarios))
print(usuarios)

print("-----------------------------------------------")

for usuario in set(assistiram):
  print(usuario)

print("-----------------------------------------------")

# teste = usuarios_data_science | usuarios_machine_learning # Unindo os dois conjuntos
teste = usuarios_data_science or usuarios_machine_learning # Unindo os dois conjuntos
print(type(teste))
print(teste)

print("---")

teste = usuarios_data_science and usuarios_machine_learning # Unindo os dois conjuntos
print(type(teste))
print(teste)

print("-----------------------------------------------")