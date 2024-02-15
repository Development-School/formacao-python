
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