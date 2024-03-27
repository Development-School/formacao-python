# -------------------------------------------------------------------- #
# 08. Interpretando listas e erros
# -------------------------------------------------------------------- #


encomendas = input("Digite os números das encomendas: ")
for encomenda in encomendas:
    print(encomenda)

print("-----------------------------------------------")

# Correto
encomendas = input("Digite os números das encomendas separados por vírgula: ").split(',')
try:
    for encomenda in encomendas:
        print(int(encomenda))
except ValueError:
    print("Uma das entradas não é um número válido.")

print("-----------------------------------------------")

encomendas = [123, 456, 789]
for encomenda in encomendas:
    print(encomenda)

print("-----------------------------------------------")

encomendas = [123, "456", 789]
for i in range(len(encomendas)):
    try:
        print(int(encomendas[i]))
    except ValueError:
        print(f"A encomenda {encomendas[i]} não é um número válido.")

print("-----------------------------------------------")

try:
    encomendas = []
    for i in range(3):
        encomendas.append(input(f"Digite o número da encomenda {i+1}: "))
except Exception as e:
    print(f"Erro: {e}")

print("-----------------------------------------------")