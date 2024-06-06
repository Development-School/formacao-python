
meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto = meu_texto.lower()

print("-----------------------------------------------")

from collections import defaultdict

aparicoes = defaultdict(int)

for palavra in meu_texto.split():
  # ate_agora = aparicoes[palavra]
  # aparicoes[palavra] = ate_agora + 1
  aparicoes[palavra] += 1

print(aparicoes)
# defaultdict(<class 'int'>, {'bem': 1, 'vindo': 1, 'meu': 2, 'nome': 1, 'é': 1, 'guilherme': 1, 'eu': 1, 'gosto': 2, 'muito': 2, 'de': 2, 'nomes': 1, 'e': 2, 'tenho': 1, 'o': 1, 'cachorro': 2})

print("-----------------------------------------------")

class Conta:
  def __init__(self):
    print("Criando uma conta")

contas = defaultdict(Conta)
print(contas[15])
# Criando uma conta
# <__main__.Conta object at 0x000002EE6A0A4E30>

print("-----------------------------------------------")

from collections import Counter # já possui o valor zero

aparicoes = Counter()
for palavra in meu_texto.split():
  aparicoes[palavra] += 1

print(aparicoes)
# Counter({'meu': 2, 'gosto': 2, 'muito': 2, 'de': 2, 'e': 2, 'cachorro': 2, 'bem': 1, 'vindo': 1, 'nome': 1, 'é': 1, 'guilherme': 1, 'eu': 1, 'nomes': 1, 'tenho': 1, 'o': 1})

print("-----------------------------------------------")

aparicoes = Counter(meu_texto.split())
print(aparicoes)
# Counter({'meu': 2, 'gosto': 2, 'muito': 2, 'de': 2, 'e': 2, 'cachorro': 2, 'bem': 1, 'vindo': 1, 'nome': 1, 'é': 1, 'guilherme': 1, 'eu': 1, 'nomes': 1, 'tenho': 1, 'o': 1})

print("-----------------------------------------------")

teste = "Hello World"
print(Counter(teste.split()))
# Counter({'Hello': 1, 'World': 1})

teste = "Hello World, Hello"
print(Counter(teste.split()))
# Counter({'Hello': 2, 'World,': 1})