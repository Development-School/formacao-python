# -------------------------------------------------------------------- #
# 07. Múltiplas referências de objetos
# -------------------------------------------------------------------- #
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

funcionario1 = Funcionario("Matheus", 5000.0)
ref_funcionario1 = funcionario1