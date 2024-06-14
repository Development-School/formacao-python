
from modelos.restaurante import Restaurante
#-------------------------------------------------------------

restaurante_praca = Restaurante('praça', 'gourmet')
restaurante_mexicano = Restaurante('mexican food', 'Mexicana')
restaurante_japones = Restaurante('japa', 'Japonesa')

#-------------------------------------------------------------

restaurante_mexicano.alternar_status()
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Lais', 8)
restaurante_praca.receber_avaliacao('Emy', 5)
#-------------------------------------------------------------
def main():
    print("-----------------------------------------------")

    Restaurante.listar_restaurantes()

    print("-----------------------------------------------")

    # ...

    print("-----------------------------------------------")

if __name__ == '__main__':
    main()