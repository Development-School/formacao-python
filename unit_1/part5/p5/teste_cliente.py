
from package.cliente import Cliente

cliente = Cliente("Marco")

print(cliente)
# <package.cliente.Cliente object at 0x000002D6F78401D0>

print(cliente.nome)
# chamando @property nome()
# Marco

print("-----------------------------------------------")

cliente.nome = 'nico' #ERRO
print(cliente.nome)
# Nico

print("-----------------------------------------------")

