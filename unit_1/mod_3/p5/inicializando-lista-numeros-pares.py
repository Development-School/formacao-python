
inteiros = [1,3,4,5,7,8,9]
pares = []

for numero in inteiros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

# ou

pares2 = [index for index in inteiros if(index % 2 == 0)]
print(pares2)