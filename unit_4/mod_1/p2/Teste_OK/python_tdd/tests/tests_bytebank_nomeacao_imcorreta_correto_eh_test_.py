
from unit_4.mod_1.p2.python_tdd.codigo.bytebank import Funcionario

#-------------------------------------------------------------

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):

        entrada = '13/03/2000' # Given-Contexto
        esperado = 22

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade() # When-ação

        assert resultado == esperado  # Then-desfecho