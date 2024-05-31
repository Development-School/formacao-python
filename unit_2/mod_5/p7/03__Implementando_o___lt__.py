class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    @property
    def codigo(self):
        return self._codigo

    @property
    def saldo(self):
        return self._saldo

    def __lt__(self, other):
        return self.saldo < other.saldo

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)

def extrai_saldo(conta):
    return conta._saldo

print("-----------------------------------------------")

conta_do_guilherme = ContaSalario(17)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(510)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

from operator import attrgetter

print(list(f'Código: {conta.codigo}, Saldo: R${conta.saldo}' for conta in sorted(contas, key=attrgetter("saldo"))))

print("-----------------------------------------------")

# print(conta_do_guilherme < conta_da_daniela) #ERROR necessário implementar __lt__
print(conta_do_guilherme < conta_da_daniela) #Após implementação do __lt__
# True

print(conta_do_guilherme > conta_da_daniela) #Após implementação do __lt__
# False

# Agora podemos ordenar de forma natural nas contas pois definimos o __lt__
print(list(conta.__str__() for conta in sorted(contas)))