import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""
    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)

        if not match:
            raise ValueError("A URL não é válida.")

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\n" + "Parâmetros: " + self.get_url_parametros() + "\n" + "URL Base: " + self.get_url_base()

    def __eq__(self, other):
        return self.url == other.url

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(url)
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)

print("-----------------------------------------------")

print("O tamanho da URL: ", len(extrator_url))

print("-----------------------------------------------")

# print(extrator_url)
# <__main__.ExtratorURL object at 0x0000023F02345520>

# Após implementação do __str__:
print(extrator_url)
# bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar
# Parâmetros: quantidade=100&moedaOrigem=real&moedaDestino=dolar
# URL Base: bytebank.com/cambio

print("-----------------------------------------------")

print(dir(str))
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__',
# '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__',
# '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__',
# '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__',
# '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold',
# 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index',
# 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric',
# 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans',
# 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition',
# 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate',
# 'upper', 'zfill']

print('__len__' in dir(str))  # Verifica se o método __len__ existe na classe str
# True

print("-----------------------------------------------")

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(url)
extrator_url_2 = ExtratorURL(url)

print(extrator_url == extrator_url_2)
# False pois os endereços de memória são diferentes

print(id(extrator_url))
# 1892847870240
print(id(extrator_url_2))
# 1892847870960

# True após implementação do __eq__

print("-----------------------------------------------")

print(1 == True)
# True

print(1 is True)
# False
print(id(1))
# 140732579841696
print(id(True))
# 140732579563344

print("-----------------------------------------------")

