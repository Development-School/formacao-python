
# from unit_4.mod_1.p2.python_tdd.codigo.bytebank import Funcionario
import pytest
from pytest import mark

# # Apenas funciona das seguintes formas:
# import os, sys # Acusa erro porém funciona  # OK!
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # OK!
# # from ..codigo.bytebank import Funcionario  # Erro!
# from codigo.bytebank import Funcionario  # Assim funciona # OK!

# from bytebank import Funcionario
# from codigo.bytebank import Funcionario # ModuleNotFoundError: No module named 'codigo'
# from .codigo.bytebank import Funcionario # ImportError: attempted relative import with no known parent package
# from ..codigo.bytebank import Funcionario # não alerta erro porém da o erro acima ao executar...

# import os
# print(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# D:\Users\Builder\Documents\Projetos e Criações\.Git\formacao-python\unit_4\mod_1\p2\python_tdd

# from ..codigo.bytebank import Funcionario # Erro
# from .codigo.bytebank import Funcionario # Erro
from codigo.bytebank import Funcionario # Alerta erro de código porém no console funciona
# from unit_4.mod_1.p2.python_tdd.codigo.bytebank import Funcionario # OK!

#-------------------------------------------------------------

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):

        entrada = '13/03/2000' # Given-Contexto
        esperado = 24

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade() # When-ação

        assert resultado == esperado  # Then-desfecho

    # @mark.skip # pula o teste
    @pytest.mark.skip(reason="não quero executar isso agora")
    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        entrada = ' Lucas Carvalho ' # Given
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, '11/11/2000', 1111)
        resultado = lucas.sobrenome() # When

        assert resultado == esperado # Then

    import sys
    @pytest.mark.skipif(sys.version_info < (3, 10), reason="Requer Python na versão 3.10 ou superior")
    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000 #given (dado, entrada)
        entrada_nome = 'Paulo Bragança'
        # entrada_nome = 'Paulo Caminha' Falha
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funcionario_teste.decrescimo_salario() # when (quando, executar algo, ação)
        resultado = funcionario_teste.salario

        assert resultado == esperado  # then (então, mostre o resultado)

    # @pytest.mark.calcular_bonus
    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000  # given
        esperado = 100

        funcionario_teste = Funcionario('teste', '11/11/2000', entrada)
        resultado = funcionario_teste.calcular_bonus()  # when

        assert resultado == esperado  # then

    # @pytest.mark.calcular_bonus
    # @mark.calcular_bonus
    @pytest.mark.xfail # Através do uso do marker xfail especificamos que o teste deve retornar uma falha, em vez de passar.
    def test_quando_calcular_bonus_recebe_100000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 100000000  # given

            funconario_teste = Funcionario('teste', '11/11/2000', entrada)
            resultado = funconario_teste.calcular_bonus()  # when

            assert resultado  # then

    # Teste desnecessário, utilizar boas práticas para que a linha 43 seja desconsiderada da cobertura de testes:
    # def test_retorno_str(self):
    #     nome, data_nascimento, salario = 'Ana', '12/03/1997', 100000000 # given
    #     esperado = 'Funcionario(Ana, 12/03/1997, 100000000)'
    #
    #     funcionario_teste = Funcionario (nome, data_nascimento, salario)
    #     resultado = funcionario_teste.__str__() # when
    #
    #     assert resultado == esperado #then