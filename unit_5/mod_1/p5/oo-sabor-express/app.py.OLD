
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
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('praça', 'Gourmet')

#-------------------------------------------------------------

def main():
    print("-----------------------------------------------")

    print(f"Avaliação teste: {restaurante_praca.media_avaliacoes}")  # Sem parênteses

    print("-----------------------------------------------")

    Restaurante.listar_restaurantes()

    print("-----------------------------------------------")

    bebida_suco = Bebida('Suco de Melancia', 5.0, 'grande')
    prato_paozinho = Prato('Paozinho', 2.00, 'O melhor pão da cidade')

    # print(bebida_suco)
    # print(prato_paozinho)
    # < modelos.cardapio.bebida.Bebida object at 0x000002826EA7FDA0 >
    # < modelos.cardapio.prato.Prato object at 0x000002826EA7E900 >

    print(bebida_suco)
    print(prato_paozinho)
    # Suco de Melancia
    # Paozinho

    print("-----------------------------------------------")

    # Métodos repetitivos... ▼
    # restaurante_praca.adicionar_bebida_no_cardapio(bebida_suco)
    # restaurante_praca.adicionar_prato_no_cardapio(prato_paozinho)

    # Refatorando...▼
    # restaurante_praca.adicionar_no_cardapio(bebida_suco)
    # restaurante_praca.adicionar_no_cardapio(prato_paozinho)
    r"""
    Traceback (most recent call last):
      File "D:\Users\Builder\Documents\Projetos e Criações\.Git\formacao-python\unit_5\mod_1\p2\oo-sabor-express\app.py", line 71, in <module>
        main()
      File "D:\Users\Builder\Documents\Projetos e Criações\.Git\formacao-python\unit_5\mod_1\p2\oo-sabor-express\app.py", line 53, in main
        restaurante_praca.adicionar_no_cardapio(bebida_suco)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AttributeError: 'Restaurante' object has no attribute 'adicionar_no_cardapio'. Did you mean: 'adicionar_prato_no_cardapio'?    
    """

    # Implementação do método: "adicionar_no_cardapio()"...
    restaurante_praca.adicionar_no_cardapio(bebida_suco)
    restaurante_praca.adicionar_no_cardapio(prato_paozinho)

    # restaurante_praca.exibir_cardapio()
    restaurante_praca.exibir_cardapio

    print("-----------------------------------------------")

    bebida_suco.aplicar_desconto()
    prato_paozinho.aplicar_desconto()

    restaurante_praca.exibir_cardapio

    print("-----------------------------------------------")

    # 08. Mão na massa - refatorando uma função ▼
    bolo_chocolate = Sobremesa('Bolo', 7.00, 'Bolo de Chocolate', 'Doce', 'grande')
    restaurante_praca.adicionar_no_cardapio(bolo_chocolate)
    restaurante_praca.exibir_cardapio

    print("-----------------------------------------------")

    # ...

    print("-----------------------------------------------")

if __name__ == '__main__':
    main()