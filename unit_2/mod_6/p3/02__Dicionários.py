
meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"

print("-----------------------------------------------")

meu_texto = set(meu_texto.split())
print(meu_texto)

print("-----------------------------------------------")

aparicoes = {
  # Chave : Valor
  "Guilherme" : 1,
  "cachorro" : 2,
  "nome" : 2,
  "vindo" : 1
}

# "Aparições traga para mim o valor da chave "Quilherme"...
print(aparicoes["Guilherme"])
# 1

# "Aparições traga para mim o valor da chave "xpto"...
# print(aparicoes["xpto"]) #Error pois não tratamos caso não exista o valor da chave informada
print(aparicoes.get("xpto", 0)) #Se não existir retorne 0
# 0

print(aparicoes.get("cachorro", 0)) #Se não existir retorne 0, porém retornará "2" pois é o valor da chave informada
# 2

print(aparicoes.get("xpto")) # Caso não informemos o valor, será tratado o erro e retornado "None"
# None

print(aparicoes.get("Guilherme")) # Caso não informemos o valor, será tratado o erro e retornado "None"
# 1

print("-----------------------------------------------")

aparicoes = dict(Guilherme = 2, cachorro = 1) # Outra forma de se instanciar dicionários
print(aparicoes)

print("-----------------------------------------------")


