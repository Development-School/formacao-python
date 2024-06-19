
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
    return (
        str(
            locale.currency(round(valor, 2),
            grouping=True
        ))  # R$ 1.000,50
    )