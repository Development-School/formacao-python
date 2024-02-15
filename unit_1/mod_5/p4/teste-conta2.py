from conta.conta import Conta

conta = Conta(123, "Nico", 55.5, 1000.0)
# Construindo objeto ... <conta.Conta object at 0x10681d588>

conta2 = Conta(321, "Marco", 100.0, 1000.0)
# Construindo objeto ... <conta.Conta object at 0x1065f0940>

print("-----------------------------------------------")

# Rotina de transferência
valor = 10.00
conta2.saca(valor)
conta.deposita(valor)

conta2.extrato()
conta.extrato()

# print("-----------------------------------------------")
#
# # Rotina de transferência implementando método para transferir
# conta = Conta(123, "Nico", 55.5, 1000.0)
# conta2 = Conta(321, "Marco", 100.0, 1000.0)
# valor = 10.00
#
# conta2.transfere(valor, conta2, conta)
# conta2.extrato()
# conta.extrato()

print("-----------------------------------------------")

# Teste de refatoração
conta = Conta(123, "Nico", 55.5, 1000.0)
conta2 = Conta(321, "Marco", 100.0, 1000.0)
valor = 10.00

conta2.transfere(valor, conta)
conta2.extrato()
conta.extrato()

print("-----------------------------------------------")