

from package.conta import Conta

conta = Conta(123, "Nico", 55.5, 1000.0)
print("-----------------------------------------------")

print(conta.saldo)

print("-----------------------------------------------")

conta.saldo = 35.5
print(conta.saldo)



