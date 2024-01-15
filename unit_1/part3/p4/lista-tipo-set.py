
lista = [11122233344, 22233344455, 33344455566]
lista.append(11122233344) #funciona!
print(lista)
# [11122233344, 22233344455, 33344455566, 11122233344]

print("-----------------------------------------------------")

colecao = {11122233344, 22233344455, 33344455566}
colecao.add(44455566677) #vai adicionar pois não existe ainda
print(colecao)

print("-----------------------------------------------------")

# print(colecao[0]) # ERRO

for tmp in colecao:
     print(tmp)

print("-----------------------------------------------------")

# Resumindo
# Um set é uma coleção não ordenada de elementos. Cada elemento é único,
# isso significa que não existem elementos duplicados dentro do set.



















