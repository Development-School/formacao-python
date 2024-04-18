# -------------------------------------------------------------------- #
# 08. Para saber mais - Outra forma de representação
# -------------------------------------------------------------------- #

import python3oo2.Modelo

# teste = Filme(nome='vingadores', ano=2018, duracao=160)

teste = python3oo2.Modelo.Filme(nome='vingadores', ano=2018, duracao=160)

print(teste)

print("-------------------Import----------------------")

lista = [1, 2, 4, 5]

print(repr(lista))

print("-----------------------------------------------")

print(repr(teste))