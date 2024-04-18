# -------------------------------------------------------------------- #
# 08. Para saber mais - Métodos estáticos e de classe
# -------------------------------------------------------------------- #

# Métodos de classe
class Funcionario:
    prefixo = 'Instrutor'

    @classmethod
    def info(cls):
        return f'Esse é um {cls.prefixo}'

print(Funcionario.info())
# Esse é um Instrutor

print("-----------------------------------------------")

# Métodos estáticos
class FolhaDePagamento:
    @staticmethod
    def log():
        return f'Isso é um log qualquer'

print(FolhaDePagamento.log())
