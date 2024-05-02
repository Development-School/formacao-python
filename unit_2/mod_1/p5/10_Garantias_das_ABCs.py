# -------------------------------------------------------------------- #
# 10. Garantias das ABCs
# -------------------------------------------------------------------- #


from collections.abc import Sized

class MinhaListagem(Sized):
    def __init__(self, descricao):
        self.descricao = descricao

    def __str__(self):
        return self.descricao

    # Implementação para corrigir erro:
    def __len__(self):
        return len(self.descricao)

lista = MinhaListagem('Nova_lista')
print(lista)
print(f'Tamanho: {len(lista)}')