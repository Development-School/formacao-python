
idades = [39,30,27,18,15] # Lista

print(idades[1])
print(idades[2])
print(idades[3])

print("-----------------------------------------------")

idades.append(15)
print(idades)
# [39,30,27,18,15]

print("-----------------------------------------------")

for idade in idades:
  print(idade)

print("-----------------------------------------------")


idades.remove(15)
print(idades)

idades.remove(30)
print(idades)
# [39,27,18,15]

print("-----------------------------------------------")

idades.append(27)
idades.remove(27)
print(idades)
# [39,18,15,27]