
pessoa1 = ("Nico", 39)
pessoa2 = ("Flavio", 37)
pessoa3 = ("Marcos", 30)

instrutores = [pessoa1, pessoa2, pessoa3]

print(instrutores)
# [('Nico', 39), ('Flavio', 37), ('Marcos', 30)]

print("-----------------------------------------------------")

print(instrutores[1][1])
# 37

print("-----------------------------------------------------")

# print(instrutores['Flavio']) #ERRO
instrutores = {'Nico' : 39, 'Flavio': 37, 'Marcos' : 30}
print(instrutores['Nico'])
# 39

print("-----------------------------------------------------")