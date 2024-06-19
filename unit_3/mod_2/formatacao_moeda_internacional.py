
import locale

print("-----------------------------------------------")

valor_inicial_em_real = 50.0
print("R$ {}".format(valor_inicial_em_real))
print("{} €".format(round(valor_inicial_em_real/6, 2)))

print("-----------------------------------------------")

#Exemplo de uso do Locale:
locale.setlocale(locale.LC_MONETARY, 'en_US.UTF-8')
valor_em_dolar_formatado = locale.currency(12.4593681)
print("Exemplo Locale: {}".format(valor_em_dolar_formatado))

print("-----------------------------------------------")

from Converte_moeda import converte_moeda

#Melhorando código (Trabalhando com a classe Converte_moeda):
print("Euro {}".format(converte_moeda(valor_inicial_em_real, 'euro')))
print("Dollar {}".format(converte_moeda(valor_inicial_em_real, 'dollar')))

print("-----------------------------------------------")

# Outro exemplo
valor_inicial_em_real = 1000.50
print(converte_moeda(valor_inicial_em_real, 'real'))
print(converte_moeda(valor_inicial_em_real, 'dollar'))

print("-----------------------------------------------")