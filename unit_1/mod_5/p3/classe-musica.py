
class Musica:

    def reproducoes(self):
        self.contador += 1

musica = Musica()
print(musica.reproducoes()) # ERROR: AttributeError: 'Musica' object has no attribute 'contador'

"""Necessário inicializar os métodos com o contrutor, __init__"""