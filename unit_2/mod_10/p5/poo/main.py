
# Ref.: (https://www.alura.com.br/artigos/python-poo-engenharia-dados)

from controller.control import *

def main():
    print("-----------------------------------------------")

    p1.mostrar_info()

    print("-----------------------------------------------")

    p2.mostrar_info()

    print("-----------------------------------------------")

    p2.mostrar_valor_total_estoque()

    print("-----------------------------------------------")

    p3.mostrar_info()
    p3.mostrar_valor_total_estoque()
    p3.mostrar_validade()  # Método novo

    print("-----------------------------------------------")

    p4.mostrar_info()
    p4.mostrar_valor_total_estoque()
    p4.mostrar_validade()  # Método sobrecarregado

    print("-----------------------------------------------")

    for i in carrinho_produtos:
        i.mostrar_info()
        print("-=" * 15)

    print("-----------------------------------------------")

if __name__ == '__main__':
    main()