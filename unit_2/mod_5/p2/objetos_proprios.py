class ContaCorrente:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return "[>>Código: {} Saldo: {}<<]".format(self.codigo, self.saldo)

print("-----------------------------------------------")

conta_do_gui = ContaCorrente(15)
print(conta_do_gui)
# [>>Codigo 15 Saldo 0<<]

print("-----------------------------------------------")

conta_do_gui.deposita(500)
print(conta_do_gui)
# [>>Codigo 15 Saldo 500<<]

print("-----------------------------------------------")

conta_da_dani = ContaCorrente(47685)
conta_da_dani.deposita(1000)
print(conta_da_dani)
# [>>Codigo 47685 Saldo 1000<<]

print("-----------------------------------------------")

contas = [conta_do_gui, conta_da_dani]
print(contas)
# [<__main__.ContaCorrente object at 0x7fabla6d40>, <__main__.ContaCorrente object at 07fabfla6db70>]

print("-----------------------------------------------")

contas = [conta_do_gui, conta_da_dani]
for conta in contas:
  print(conta)

# [>>Codigo 15 Saldo 500<<]
# [>>Codigo 47685 Saldo 1000<<]

print("-----------------------------------------------")

contas = [conta_do_gui, conta_da_dani, conta_do_gui]
print(contas[0])
# [>>Codigo 15 Saldo 500<<]

print([conta.__str__() for conta in contas])

print("-----------------------------------------------")

conta_do_gui.deposita(100)
print(contas[0])
# [>>Codigo 15 Saldo 600<<]

print([conta.__str__() for conta in contas])

print("-----------------------------------------------")

contas[2].deposita(300)
print([conta.__str__() for conta in contas])
print(contas[2].saldo)
print(conta_do_gui.saldo)

print("-----------------------------------------------")