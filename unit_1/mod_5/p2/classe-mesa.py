# -------------------------------------------------------------------- #
# 08. Criando objetos no Serenatto Café & Bistrô
# -------------------------------------------------------------------- #
class Mesa:

    def __init__(self, numero, capacidade, ocupada):
        self.numero = numero
        self.capacidade = capacidade
        self.ocupada = ocupada

lais = Mesa(numero=1234, capacidade=6, ocupada=False)
print(lais.numero)