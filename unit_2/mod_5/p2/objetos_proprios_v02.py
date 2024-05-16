class ContaCorrente:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return "[>>Código: {} Saldo: {}<<]".format(self.codigo, self.saldo)

def deposita_para_todas(contas):
  for conta in contas:
      conta.deposita(100)

def deposita(conta): # variação "funcional" (separando o comportamento dos dados)
    novo_saldo = conta[1] + 100
    codigo = conta[0]
    return (codigo, novo_saldo)

print("-----------------------------------------------")

conta_do_gui = ContaCorrente(15)
conta_da_dani = ContaCorrente(47685)

contas = [conta_do_gui, conta_da_dani]
print([conta.__str__() for conta in contas])

print("-----------------------------------------------")

deposita_para_todas(contas)
print(contas[0], contas[1])
# [>>Codigo 15 Saldo 900<<] [>>Codigo 47685 Saldo 1000<<]
# [>>Codigo 15 Saldo 1000<<] [>>Codigo 57685 Saldo 1100<<]

print("-----------------------------------------------")

contas.insert(0,76)
print(contas[0], contas[1], contas[2])
# 76 [>>Código: 15 Saldo: 100<<] [>>Código: 47685 Saldo: 100<<]

# deposita_para_todas(contas) #Error pois não podemos fazer "76.deposita()"
# print(contas[0], contas[1], contas[2])

print("-----------------------------------------------")

# [Guilherme', 37]
# [Daniela, 31]

usuarios = ['Guilherme', 37]
print(usuarios)

# usuarios.append('Daniela', 31) #error pois uma coleção do tipo "tupla" são imutáveis. Não é possível alterá-los

usuarios = ('Guilherme', 37) #tupla
print(usuarios)

guilherme = ('Guilherme', 37, 1981)
daniela = ('Daniela', 31, 1987)
print(guilherme, daniela)

print("-----------------------------------------------")

conta_do_gui = (15, 1000)
print(conta_do_gui)

print("-----------------------------------------------")

print(deposita(conta_do_gui))
print(conta_do_gui)

print("-----------------------------------------------")

conta_do_gui = deposita(conta_do_gui)
print(conta_do_gui)

print("-----------------------------------------------")

