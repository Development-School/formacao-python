# -------------------------------------------------------------------- #
# Python: Trabalhando com precisão em números decimais
# -------------------------------------------------------------------- #

ganhos_julho = 99.91 * 5
print(ganhos_julho)
# 499.54999999999995

gastos_julho = 110.1 * 3
print(gastos_julho)
# 330.29999999999995

print("-----------------------------------------------")

from decimal import Decimal

ganhos_julho = Decimal('99.91') * 5
print(ganhos_julho)

gastos_julho = Decimal('110.1') * 3
print(gastos_julho)

print("-----------------------------------------------")