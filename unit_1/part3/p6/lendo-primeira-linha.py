# -------------------------------------------------------------------- #
# 06. Lendo a primeira linha
# -------------------------------------------------------------------- #

arquivo = open('pessoas.txt', 'w')
arquivo.write("Romário 37\nJunior 32\nDaniel 28\nIzzy 38")
arquivo.close()

arquivo = open('pessoas.txt', 'r')
print(arquivo.read())
arquivo.close()

"""
Romário 37
Junior 32
Daniel 28
Izzy 38
"""

print("-----------------------------------------------\n")

arquivo = open("pessoas.txt", 'r')
print(arquivo.readline().strip())
arquivo.close()

