print("-----------------------------------------------")

lista = [1, 2, 3, 4]
for i in lista:
    print(i)

print("-----------------------------------------------")

conjunto = {'Lucas' : 40, 'Karla' : '41'}

#fechado, compactado
for i in conjunto:
    print(i)

print("-----------------------------------------------")

#abrindo, descompactanto - unpack
for i1, i2  in conjunto.items():
    print(i1, i2)

print("-----------------------------------------------")