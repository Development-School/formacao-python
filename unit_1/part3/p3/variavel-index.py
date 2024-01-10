# -------------------------------------------------------------------- #
# 07. Para saber mais - Variável index
# -------------------------------------------------------------------- #

numeros = [10, 20, 30, 40, 50]

for i in range(len(numeros)):
    print("O elemento na posição", i, "é", numeros[i])

# for i in len(numeros): #ERRO
#     print("O elemento na posição", i, "é", numeros[i])

# for i in numeros: #ERRO
#     print("O elemento na posição", i, "é", numeros[i])

frase = "Olá, mundo!"

print("+++++++++++++++++++++++++")

for i in range(len(frase)):
    print("O caractere na posição", i, "é", frase[i])