# -------------------------------------------------------------------- #
# 09. Para saber mais - with
# -------------------------------------------------------------------- #


logo = open('palavras.txt', 'r')
data = logo.read()
logo.close()

with open("palavras.txt") as arquivo:
    for linha in arquivo:
        print(linha)

arquivo.close()

print("-----------------------------------------------\n")

with open("palavras.txt") as arquivo:
    print(arquivo.read())
arquivo.close()
















































