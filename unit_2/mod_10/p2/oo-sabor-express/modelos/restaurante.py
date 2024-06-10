class Restaurante:
    restaurantes = []

    #Construtor ▼
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.status = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

    @staticmethod
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.status}')