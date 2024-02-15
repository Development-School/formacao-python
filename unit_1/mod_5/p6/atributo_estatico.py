# -------------------------------------------------------------------- #
# 12. Para saber mais - Atributo estático
# -------------------------------------------------------------------- #



class Circulo:

    @staticmethod
    def obter_pi():
        return 3.14

print(Circulo.obter_pi())
# 3.14

print("-----------------------------------------------")

class Circulo2:

    PI = 3.14

print(Circulo2.PI)
# 3.14