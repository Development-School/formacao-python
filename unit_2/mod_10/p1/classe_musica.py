
class Musica:
    nome = ''
    artista = ''
    duracao = int

musica1 = Musica()
musica1.nome = 'Bohemian Rhapsody'
musica1.artista = 'Queen'
musica1.duracao = 355

musica2 = Musica()
musica2.nome = 'Imagine'
musica2.artista = 'John Lennon'
musica2.duracao = 183

musica3 = Musica()
musica3.nome = 'Shape of You'
musica3.artista = 'Ed Sheeran'
musica3.duracao = 234

print("-----------------------------------------------")

musicas = [musica1, musica2, musica3]

for i in musicas:
    print(i.nome, i.artista, i.duracao)

print("-----------------------------------------------")

print(f'Música: {musica1.nome} - '
      f'Banda: {musica1.artista} - '
      f'{musica1.duracao} segundos')


print("-----------------------------------------------")