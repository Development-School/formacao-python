
class Livro:
    def __init__(self, titulo, autor, data_de_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.data_de_publicacao = data_de_publicacao

livro = Livro("Amor e Trovão", "Marvel", data_de_publicacao="23/01/2024")
print("{}, poublicado em {}".format(livro.titulo, livro.data_de_publicacao))