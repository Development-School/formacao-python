import locale

def converte_moeda(valor, moeda):
    # locale.setlocale(locale.LC_MONETARY, 'en_US.UTF-8') #Dollar
    if(moeda == 'euro'):
        locale.setlocale(locale.LC_MONETARY, 'it_IT.UTF-8')  # Euro
        valor = (valor/6)
    elif(moeda == 'dollar'):
        locale.setlocale(locale.LC_MONETARY, 'en_US.UTF-8')  # Dollar
        valor = (valor / 5)
    elif(moeda == 'real'):
        locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')  # Real
        valor = valor

    # return str(locale.currency(round(valor, 2))) # R$ 1000,50
    return str(locale.currency(round(valor, 2), grouping=True)) # R$ 1.000,50

valor_inicial_em_real = 50.0
print("R$ {}".format(valor_inicial_em_real))
print("{} €".format(round(valor_inicial_em_real/6, 2)))

print("-----------------------------------------------")

#Exemplo de uso do Locale:
locale.setlocale(locale.LC_MONETARY, 'en_US.UTF-8')
valor_em_dolar_formatado = locale.currency(12.4593681)
print("Exemplo de uso do Locale: {}".format(valor_em_dolar_formatado))

print("-----------------------------------------------")

#Melhorando código:
print("Euro {}".format(converte_moeda(valor_inicial_em_real, 'euro')))
print("Dollar {}".format(converte_moeda(valor_inicial_em_real, 'dollar')))

print("-----------------------------------------------")

# Outro exemplo
valor_inicial_em_real = 1000.50
print(converte_moeda(valor_inicial_em_real, 'real'))
print(converte_moeda(valor_inicial_em_real, 'dollar'))

print("-----------------------------------------------")