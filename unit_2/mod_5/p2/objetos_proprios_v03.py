class ContaCorrente:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return "[>>Código: {} Saldo: {}<<]".format(self.codigo, self.saldo)

guilherme = ('Guilherme', 37, 1981)
daniela = ('Daniela', 31, 1987)

usuarios = [guilherme, daniela]
print(usuarios)

print("-----------------------------------------------")

usuarios.append(('Paulo', 39, 1979))
print(usuarios)

print("-----------------------------------------------")

# usuarios[0][0] = 'Guilherme Silveira' #erro pois a lista está composta de tuplas e tuplas são imutáveis
print(usuarios[0][0])

print("-----------------------------------------------")

conta_do_gui = ContaCorrente(15)
conta_da_dani = ContaCorrente(47685)

conta_do_gui.deposita(500)
conta_da_dani.deposita(1000)

print([conta.__str__() for conta in [conta_do_gui, conta_da_dani]])

print("-----------------------------------------------")

contas = [conta_do_gui, conta_da_dani]
print([conta.__str__() for conta in contas])

contas[0].deposita(500)
print([conta.__str__() for conta in contas])

print("-----------------------------------------------")

contas = (conta_do_gui, conta_da_dani)
print([conta.__str__() for conta in contas])

contas[0].deposita(1000)
print([conta.__str__() for conta in contas])

print("-----------------------------------------------")

