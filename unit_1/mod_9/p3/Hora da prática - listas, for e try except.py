# -------------------------------------------------------------------- #
# 10. Hora da prática - listas, for e try except
# -------------------------------------------------------------------- #


# 1 - Para criar as listas, podemos utilizar as seguintes variáveis:

lista_de_numeros = [1,2,3,4,5,6,7,8,9,10]
lista_de_nomes = ['emy','gui','lais','mari']
lista_de_anos = [1999,2023]

# 2 - Para percorrer todos os itens de uma lista com o loop for, você pode usar essa estrutura:

lista_de_numeros = [1,2,3,4,5,6,7,8,9,10]
for numero in lista_de_numeros:
    print(numero)

print("-----------------------------------------------")

# 3 - Para fazer calcular a soma dos números impares de 1 a 10, você pode utilizar o seguinte código:

soma_impares = 0
for i in range(1, 11, 2):
    soma_impares += i
print(soma_impares)

"""O segundo argumento de da função range é exclusivo, então range(1, 11) inclui números de 1 a 10) com um passo de 2 (o terceiro argumento de range).
Isso garante que apenas números ímpares sejam considerados."""

print("-----------------------------------------------")

# 4 - Para imprimir os números de 1 a 10 de forma decrescente, você pode utilizar a seguinte estrutura:

for i in range(10, 0, -1):
    print(i)

print("-----------------------------------------------")

# 5 - Para fazer uma tabuada interativa, você pode seguir o seguinte código:

numero_tabuada = int(input("Digite um número para a tabuada: "))
for i in range(1, 11):
    resultado = numero_tabuada * i
    print(f"{numero_tabuada} x {i} = {resultado}")

print("-----------------------------------------------")

# 6 - Uma possível resolução para fazer a soma dos elementos de uma lista com for e usar try except para validar, está no código a seguir:

lista_numeros = [10, 5, 8, 3, 7]
soma = 0

try:
    for numero in lista_numeros:
        soma += numero
    print(f"Soma dos elementos: {soma}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

"""Exception é uma classe base para todas as exceções em Python. Capturar Exception permite lidar com qualquer tipo de exceção que possa ocorrer no bloco try.
O as e é opcional, mas é frequentemente usado para acessar informações detalhadas sobre a exceção, como mensagens de erro."""

print("-----------------------------------------------")

# 7 - Um modo de solucionar essa questão com uma validação de lista vazia é do seguinte modo:

lista_valores = [15, 20, 25, 30]
soma_valores = 0

try:
    for valor in lista_valores:
        soma_valores += valor
    media = soma_valores / len(lista_valores)
    print(f"Média dos valores: {media}")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

# ZeroDivisionError é uma exceção específica que ocorre quando há uma tentativa de divisão por zero. Este bloco except é destinado a lidar

print("-----------------------------------------------")