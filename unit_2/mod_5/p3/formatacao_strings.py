
num = 7.123456

print("%1.2f " % num)
print("{:.2f}".format( num ))

print("-----------------------------------------------")

num = 1.672500

print("%.1f" % num)
print("%.2f" % num)

print("-----------------------------------------------")

saldo = float(345)
print(f'Saldo inicial: R$ {saldo}')
print('Saldo inicial: R$ {}'.format('%.2f' % saldo,))
print('Saldo inicial: R$ {:.2f}'.format(saldo))
print('{} inicial: R$ {:.2f}'.format('saldo'.title(), saldo))

print("-----------------------------------------------")

print(format(42, 'f'))
print(type(format(42, 'f')))

print("-----------------------------------------------")

from decimal import Decimal

print(f'Saldo inicial: R$ {saldo}')
print(f'Saldo inicial: R$ {Decimal(saldo).quantize(Decimal("0.00"))}')

