

from package.conta import Conta

conta = Conta(123, "Nico", 55.5, 1000.0)
print("-----------------------------------------------")

print(conta.get_titular())
print(conta.get_saldo())
print(conta.limite)

print("-----------------------------------------------")

conta.limite = 10000.0
print(conta.limite)
