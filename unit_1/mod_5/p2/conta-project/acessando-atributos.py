from conta import Conta

conta = Conta(123, "Nico", 55.5, 1000.0)
# Construindo objeto ... <conta.Conta object at 0x10293ae48>

conta2 = Conta(321, "Marco", 100.0, 1000.0)
# Construindo objeto ... <conta.Conta object at 0x10293acf8>

print(conta)
print(conta2)

print("-----------------------------------------------")

print(conta.titular)
print(conta2.titular)

print("-----------------------------------------------")

print(conta.saldo)
# 55.5
print(conta2.saldo)
# 100.0

print("-----------------------------------------------")