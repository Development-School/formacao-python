

class Menu:
    catalogo = {}

    def adicionar_item(self, item, ingredientes):
        self.catalogo[item] = ingredientes

    @staticmethod
    def ingredientes(item):
        return Menu.catalogo[item]

m = Menu

m.catalogo = {'Farofa', 'Arroz', 'Carne'}
print(m.catalogo)

print("-----------------------------------------------")

m.catalogo.add('Peixe')
print(m.catalogo)

print("-----------------------------------------------")

m.ingredientes = {'Farinha'}
print(m.ingredientes)

print("-----------------------------------------------")

m.ingredientes.add('Sal')
m.ingredientes.add('Açucar')
print(m.ingredientes)