
class Pessoa:
    def __init__(self, nome, idade, cpf):
        self._nome = nome
        self._idade = idade
        self._cpf = cpf

    @property
    def getNome(self):
        return self._nome

    @getNome.setter
    def setNome(self, nome):
        self._nome = nome

    @property
    def getCpf(self):
        return self._cpf

    @getCpf.setter
    def setCpf(self, cpf):
        self._cpf = cpf

    @property
    def getIdade(self):
        return self._idade

    @getIdade.setter
    def setIdade(self, idade):
        self._idade = idade

    def __str__(self):
        return f'Nome: {self.getNome }, ' \
               f'Idade: {self.getIdade}, ' \
               f'Cpf: {self.getCpf}'

print("-----------------------------------------------")

lucas = Pessoa("Marcio Lucas Mota Caminha", None, None)
print(lucas)

print("-----------------------------------------------")

lucas.setNome = "Lucas Caminha"
lucas.setIdade = 40
lucas.setCpf = '002.980.643-75'
print(lucas)

print("-----------------------------------------------")

print(lucas.getNome)
print(lucas.getIdade)
print(lucas.getCpf)

print("-----------------------------------------------")

print(vars(lucas))
# {'_nome': 'Lucas Caminha', '_idade': 40, '_cpf': '002.980.643-75'}

print("-----------------------------------------------")