
vendedores = ["Marcus", "Amanda", "Ale", "Carol"]
vendas = [15, 20, 10, 30]

# Objetivo:
# Vendedor 1: Marcus - 15 Produtos
# Vendedor 2: Amanda - 20 Produtos
# ...

print("-----------------------------------------------")

# Zip uni as duas estruturas iterables em uma apenas
# e faz o processo de interação semelhante ao enumerate...
for vendedor, venda in zip(vendedores, vendas):
    print(vendedor, venda)

print("-----------------------------------------------")

i = 0
for vendedor, venda in zip(vendedores, vendas):
    print(f"Vendedor {i + 1}: {vendedor.ljust(10)} | Venda: {venda}")
    i += 1

print("-----------------------------------------------")