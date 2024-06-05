
usuarios = {1,5,76,34,52,13,17}
print(len(usuarios))

print("-----------------------------------------------")

# Tentar adicionar usuários com append() vai dar erro o correto em conjuntos é utilizar o add()
# usuarios.append(14) #error

teste = list(usuarios)
teste.append(14) #error
print(len(teste))

print("-----------------------------------------------")

usuarios.add(14)
print(len(usuarios))

usuarios.add(13) # Como já existe o 13 em conjuntos ele não duplica valores iguais
print(len(usuarios))
print(usuarios)

print("-----------------------------------------------")

usuarios.add(765)
print(len(usuarios))
print(usuarios)

print("-----------------------------------------------")

# Criando conjuntos congelados
usuarios_congelado = frozenset(usuarios)
# usuarios_congelado.add(99) #Erro não é possível adicionar elementos em conjuntos congeleados
print(usuarios_congelado)
print(type(usuarios_congelado))

print("-----------------------------------------------")

meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
# print(meu_texto.split(" "))
# Ou ▼
print(meu_texto.split())
# ['Bem', 'vindo', 'meu', 'nome', 'é', 'Guilherme', 'eu', 'gosto', 'muito', 'de', 'nomes', 'e', 'tenho', 'o', 'meu', 'cachorro', 'e', 'gosto', 'muito', 'de', 'cachorro']

# print(meu_texto.split("_"))
# ['Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro']

print("-----------------------------------------------")

meu_texto = set(meu_texto.split())
print(meu_texto)
# {'e', 'Bem', 'Guilherme', 'nomes', 'gosto', 'vindo', 'tenho', 'cachorro', 'de', 'nome', 'meu', 'o', 'eu', 'é', 'muito'}