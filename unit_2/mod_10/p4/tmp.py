
from modelos.restaurante import Restaurante
#-------------------------------------------------------------

restaurante_praca = Restaurante('praça', 'gourmet')
restaurante_mexicano = Restaurante('mexican food', 'Mexicana')
restaurante_japones = Restaurante('japa', 'Japonesa')

#-------------------------------------------------------------
def main():
    print("-----------------------------------------------")

    Restaurante.listar_restaurantes()

    print("-----------------------------------------------")

    restaurante_mexicano.alternar_status()
    Restaurante.listar_restaurantes()

    print("-----------------------------------------------")

    restaurante_praca.receber_avaliacao('Gui', 10)
    restaurante_praca.receber_avaliacao('Lais', 8)
    restaurante_praca.receber_avaliacao('Emy', 5)
    Restaurante.listar_restaurantes()

    print("-----------------------------------------------")

    # restaurante_praca.media_avaliacoes()
    # for avaliacao in restaurante_praca.getAvaliacao:
    #     print(avaliacao._nota)
    #
    # media = (
    #     sum(avaliacao._nota for avaliacao in restaurante_praca.getAvaliacao)
    #     /
    #     len(restaurante_praca.getAvaliacao)
    # )
    # print(round(media, 1))

    # print(restaurante_praca.media_avaliacoes())
    # print(restaurante_mexicano.media_avaliacoes())

    Restaurante.listar_restaurantes()

print("-----------------------------------------------")

if __name__ == '__main__':
    main()