# -------------------------------------------------------------------- #
# 04. Entendendo encapsulamento na classe Retângulo
# -------------------------------------------------------------------- #

class Retangulo:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__area = x * y

    def obter_area(self):
        return self.__area

r = Retangulo(7,6)
r.area = 7 #Não acusa ERRO, porém não será atribuido valor a variável "área" pois o atributo está como privado.
print(r.obter_area())
