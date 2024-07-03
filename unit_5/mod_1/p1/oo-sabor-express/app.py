
from modelos.restaurante import Restaurante
#-------------------------------------------------------------

# Exemplo de uso
restaurante_praca = Restaurante('praça', 'gourmet')
restaurante_mexicano = Restaurante('mexican food', 'Mexicana')
restaurante_japones = Restaurante('japa', 'Japonesa')

#-------------------------------------------------------------

restaurante_mexicano.alternar_status()
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Lais', 8)
restaurante_praca.receber_avaliacao('Emy', 5)

#-------------------------------------------------------------

# from modelos.cardapio.item_cardapio import ItemCardapio
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida ('Suco de Melancia', 5.0, 'grande')
prato_paozinho = Prato('Paozinho', 2.00, 'O melhor pão da cidade')

#-------------------------------------------------------------

def main():
    print("-----------------------------------------------")

    print(f"Avaliação teste: {restaurante_praca.media_avaliacoes}")  # Sem parênteses

    print("-----------------------------------------------")

    Restaurante.listar_restaurantes()

    print("-----------------------------------------------")

    # print(bebida_suco)
    # print(prato_paozinho)
    # < modelos.cardapio.bebida.Bebida object at 0x000002826EA7FDA0 >
    # < modelos.cardapio.prato.Prato object at 0x000002826EA7E900 >

    print(bebida_suco)
    print(prato_paozinho)
    # Suco de Melancia
    # Paozinho

    print("-----------------------------------------------")

    # ...

    print("-----------------------------------------------")

    # ...

    print("-----------------------------------------------")

    # ...

    print("-----------------------------------------------")

    # ...

    print("-----------------------------------------------")

if __name__ == '__main__':
    main()