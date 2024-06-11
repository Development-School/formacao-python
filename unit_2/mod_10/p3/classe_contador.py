class Contador:
    '''
    Classe que representa um contador.
    A instância mantém um contador específico, enquanto um contador global é compartilhado por todas as instâncias.
    '''

    contador_global = 0

    def __init__(self):
        self.valor = 0

    def __str__(self):
        return f'Contador:  {self.valor}\n' \
               f'Contador Global: {Contador.contador_global}'

    def incrementar(self):
        self.valor += 1
        Contador.contador_global += 1

    def zerar_valor(self):
        self.valor = 0
        print('Valor foi zerado.')

    @classmethod
    def zerar_contador_global(cls):
        cls.contador_global = 0
        print('Contador global foi zerado.')

print("-----------------------------------------------")

teste = Contador()
print(teste)

print("-----------------------------------------------")

teste.incrementar()
teste.incrementar()
print(teste)

print("-----------------------------------------------")

teste.zerar_contador_global()
print(teste)

print("-----------------------------------------------")

teste.incrementar()
teste.incrementar()
print(teste)

print("-----------------------------------------------")

teste.zerar_valor()
print(teste)

print("-----------------------------------------------")

# ...

print("-----------------------------------------------")

# ...

print("-----------------------------------------------")

# ...

print("-----------------------------------------------")