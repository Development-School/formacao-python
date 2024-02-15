
class Menu:
    catalogo = {}

    def adicionar_item(self, item, ingredientes):
        self.catalogo[item] = ingredientes

    @staticmethod
    def ingredientes(item):
        return Menu.catalogo[item]

Menu.adicionar_item(Menu, 'Agua', 'Água natual sem gás')
print("O item {} possui os seguintes igredientes: {}".format("??", Menu.ingredientes('Agua')))

print("-----------------------------------------------")

