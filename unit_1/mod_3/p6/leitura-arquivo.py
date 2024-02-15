# -------------------------------------------------------------------- #
# 05. Lendo um arquivo
# -------------------------------------------------------------------- #

arquivo = open("palavras.txt", "r")
print(arquivo.read())
# 'banana\nmelancia\nmorango\nmanga\n'

print("-----------------------------------------------\n")

print(arquivo.read())
# ''

print("-----------------------------------------------\n")

# Lendo linha por linha do arquivo
arquivo = open("palavras.txt", "r")
for linha in arquivo:
    print(linha)
"""
banana

melancia

morango

manga
"""

print("-----------------------------------------------\n")

arquivo = open("palavras.txt", "r")
linha = arquivo.readline()
print(linha)
# 'banana\n'

# Limpando a linha
print(linha.strip())
# 'banana'















