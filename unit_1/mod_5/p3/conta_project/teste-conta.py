from conta import Conta

conta = Conta(123, "Nico", 55.5, 1000.0)
# Construindo objeto ... <conta.Conta object at 0x10db29e80>

conta.extrato()
# Saldo de 55.5 do titular Nico

print("-----------------------------------------------")

conta.deposita(15.0)
conta.extrato()
# Saldo de 70.5 do titular Nico

print("-----------------------------------------------")

conta.saca(10.0)
conta.extrato()
# Saldo de 60.5 do titular Nico

print("-----------------------------------------------")