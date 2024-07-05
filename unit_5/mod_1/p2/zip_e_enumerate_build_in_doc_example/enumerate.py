
vendedores = ["Marcus", "Amanda", "Ale", "Carol"]
vendas = [15, 20, 10, 30]

# Objetivo:
# Vendedor 1: Marcus - 15 Produtos
# Vendedor 2: Amanda - 20 Produtos
# ...

print("-----------------------------------------------")

for vendedor in vendedores:
        print(vendedor)

print("-----------------------------------------------")

# tamanho_lista = len(vendedores)
# for i in range(tamanho_lista):
for i in range(len(vendedores)):
    print(vendedores[i])
    print(vendas[i])

# Marcus
# Amanda
# Ale
# Carol
# Marcus
# 15
# Amanda
# 20
# Ale
# 10
# Carol
# 30

print("-----------------------------------------------")

# Por padrão o enumerate inicia com zero (start=0)
for i, vendedor in enumerate(vendedores):
    print(f"Vendedor {i + 1}: {vendedor.ljust(10)} | Venda: {vendas[i]}")

# Vendedor 01: Marcus     | Venda: 15
# Vendedor 02: Amanda     | Venda: 20
# Vendedor 03: Ale        | Venda: 10
# Vendedor 04: Carol      | Venda: 30

print("-----------------------------------------------")

for i, vendedor in enumerate(vendedores, start=1):
    print(f"Vendedor {i}: {vendedor.ljust(10)} | Venda: {vendas[i - 1]}")

print("-----------------------------------------------")