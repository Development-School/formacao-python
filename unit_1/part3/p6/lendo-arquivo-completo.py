# -------------------------------------------------------------------- #
# 07. Lendo um arquivo por completo
# -------------------------------------------------------------------- #

"""
Banana
Maçã
Pera
Uva
Jamelão
"""
arquivo = open('frutas.txt', 'w')
arquivo.write("Banana\nMaçã\nPera\nUva\nJamelão")
arquivo.close()

# arquivo = open('frutas.txt', 'r')
# ou
arquivo = open('frutas.txt')
print(arquivo.read())
arquivo.close()

print("-----------------------------------------------\n")

arquivo = open("frutas.txt")
linha = arquivo.readline()
print(linha)

linha = arquivo.readline()
print(linha)
arquivo.close()

print("-----------------------------------------------\n")

arquivo = open('frutas.txt','r')
conteudo = arquivo.read()
print(conteudo)

conteudo = arquivo.read()
print(conteudo)

arquivo.close()

