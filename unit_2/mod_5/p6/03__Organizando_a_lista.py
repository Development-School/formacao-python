

idades = [15, 87, 32, 65, 56, 32, 49, 37]

# print(list(idades))
print(idades)
# [15, 87, 32, 65, 56, 32, 49, 37]

print("-----------------------------------------------")

print(list(reversed(idades)))
# [37, 49, 32, 56, 65, 32, 87, 15]

print("-----------------------------------------------")

#Ordenando utilizando Sorted
print(sorted(idades))
# [15, 32, 32, 37, 49, 56, 65, 87]

print("-----------------------------------------------")

#Imprimindo o inverso utilizando reversed + sorted
print(list(reversed(sorted(idades))))
# [87, 65, 56, 49, 37, 32, 32, 15]

#Imprimindo o inverso utilizando Sorted com parâmetro
print(sorted(idades, reverse=True))
# [15, 32, 32, 37, 49, 56, 65, 87]

print("-----------------------------------------------")

print(idades)
print(idades.sort()) # NEsse momento do código ele "chumba" a ordenação
print(idades)

print("-----------------------------------------------")

print(idades)
idades.reverse()
print(idades)

print("-----------------------------------------------")