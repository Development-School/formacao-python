# -------------------------------------------------------------------- #
# 08. Loop relativo à List Comprehension
# -------------------------------------------------------------------- #


frutas = ["maçã", "banana", "laranja", "melancia"]
print(frutas)

lista = []
for fruta in frutas: lista.append(fruta.upper())
print(lista)

lista2 = [index.upper() for index in frutas]
print(lista2)

