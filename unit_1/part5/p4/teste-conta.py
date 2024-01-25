from conta.conta import Conta

conta = Conta(123, "Nico", 55.5, 1000.0)
# Construindo objeto ... <conta.Conta object at 0x10db29e80>

# print(conta.saldo) # Erro pois o atributo agora está como privado

conta.extrato()