# -------------------------------------------------------------------- #
# 03. Funções importantes
# -------------------------------------------------------------------- #

valores = ("a","b","c","d","e")
print(len(valores))
# 5

print(max(valores))
# e

# print(del(valores[0])) #ERRO
#Corrigindo: Alterar de "tupla" para "lista"
valores = ["a","b","c","d","e"]
print(valores)
# ["a","b","c","d","e"]

del(valores[0]) #funciona pois é lista
print(valores)
# ['b', 'c', 'd', 'e']

# erro

print(min(valores))
# b