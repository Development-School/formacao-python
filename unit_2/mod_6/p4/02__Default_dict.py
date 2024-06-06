
meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto = meu_texto.lower()

print(meu_texto)

print("-----------------------------------------------")

aparicoes = {}

for palavra in meu_texto.split():
  # ate_agora = aparicoes[palavra] # Error
  ate_agora = aparicoes.get(palavra, 0)
  aparicoes[palavra] = ate_agora + 1

print(aparicoes)
# {'bem': 1, 'vindo': 1, 'meu': 2, 'nome': 1, 'é': 1, 'guilherme': 1, 'eu': 1, 'gosto': 2, 'muito': 2, 'de': 2, 'nomes': 1, 'e': 2, 'tenho': 1, 'o': 1, 'cachorro': 2}

print("-----------------------------------------------")

print(int(15))
# 15
print(int())
# 0
print(int)
# <class 'int'>

print("-----------------------------------------------")

# DefaultDict muito utilizado para retornar algo quando não encontrar a chave pesquisada
from collections import defaultdict

aparicoes = defaultdict(int)

for palavra in meu_texto.split():
  # ate_agora = aparicoes.get(palavra, 0)
  ate_agora = aparicoes[palavra]
  aparicoes[palavra] = ate_agora + 1

print(aparicoes)
# defaultdict(<class 'int'>, {'bem': 1, 'vindo': 1, 'meu': 2, 'nome': 1, 'é': 1, 'guilherme': 1, 'eu': 1, 'gosto': 2, 'muito': 2, 'de': 2, 'nomes': 1, 'e': 2, 'tenho': 1, 'o': 1, 'cachorro': 2})

print("-----------------------------------------------")

dicionario = defaultdict(int)
print(dicionario['guilherme'])
# 0

dicionario['guilherme'] = 15
print(dicionario['guilherme'])
# 15

print("-----------------------------------------------")