
# from unit_4.mod_1.p2.python_tdd.codigo.bytebank import Funcionario

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