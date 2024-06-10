class Musica:

    musicas = []

    def __init__(self, nome='', artista='', duracao=0):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)

    @staticmethod
    def listar_musicas():
        for musica in Musica.musicas:
            print(f'{musica.nome} | {musica.artista} | '
                  f'{musica.duracao}')

print("-----------------------------------------------")

musica1 = Musica(nome='Under Pressure', artista='Queen & David Bowie', duracao=248)
musica2 = Musica(nome='The Trooper', artista='Iron Maiden', duracao=245)
musica3 = Musica(nome='Hotel California', artista='Eagles', duracao=390)
musica4 = Musica()
musica5 = Musica()
musica6 = Musica()

Musica.listar_musicas()

print("-----------------------------------------------")