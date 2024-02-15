# -------------------------------------------------------------------- #
# 07. Implementação de métodos estáticos
# -------------------------------------------------------------------- #


# class Pagamento:
#     def __init__(self, horas, taxa):
#         self.horas = horas
#         self.taxa = taxa
#
#     def calcular_pagamento(self):
#         return self.horas * self.taxa
#
# pagamento = Pagamento(40, 15)
# print(pagamento.calcular_pagamento())

# class Pagamento:
#     @staticmethod
#     def calcular_pagamento(horas, taxa):
#         return horas * taxa
#
# pagamento = Pagamento()
# print(pagamento.calcular_pagamento(40, 15))

#ERRO
# class Pagamento:
#     @staticmethod
#     def __calcular_pagamento(horas, taxa):
#         return horas * taxa
#
# print(Pagamento.__calcular_pagamento(40, 15))
#ERRO

class Pagamento:
    @staticmethod
    def calcular_pagamento(horas, taxa):
        return horas * taxa

print(Pagamento.calcular_pagamento(40, 15))