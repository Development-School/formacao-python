class Sapataria:
    sapatarias = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Sapataria.sapatarias.append(self)

    def __str__(self):
        return f'{self.nome}|{self.categoria}'

    @staticmethod
    def listar_sapatarias():
        for sapataria in Sapataria.sapatarias:
            print(f'{sapataria.nome}|{sapataria.categoria}|{sapataria.ativo}')

sapataria_praca = Sapataria('uva', 'meu')
sapataria_coro = Sapataria('meu mel', 'curva')

print("-----------------------------------------------")

Sapataria.listar_sapatarias()

print("-----------------------------------------------")