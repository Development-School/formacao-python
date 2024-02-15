
class Apresentacao:

    def __init__(self, horario, banda):
        self.__horario = horario
        self.__banda = banda

    @property
    def horario(self):
        return self.__horario

    @horario.setter
    def horario(self, horario):
        self.__horario = horario

    @property
    def banda(self):
        return self.__banda

    @banda.setter
    def banda(self, banda):
        self.__banda = banda


a = Apresentacao("02:40", "Gun's and Roses")
print("Apresentação da banda {} será às {}.".format(a.banda, a.horario))

print("-----------------------------------------------")

a.banda = "\"Gun's and Roses\""
a.horario = '03:00'

print("Nova programação da banda {} será às {}.".format(a.banda, a.horario))