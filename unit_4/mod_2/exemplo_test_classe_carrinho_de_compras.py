import pytest
import unittest

from src.compras import CarrinhoDeCompras, ItemDoCarrinho, Usuario

class TestCarrinhoDeCompras:
    """
    Quando decoramos uma função, ou método, com @pytest.fixture, por padrão,
    essa função é executada antes de cada método de teste que precise dela. Ou seja,
    para cada vez que o teste é rodado, um novo objeto é instanciado na memória e
    é utilizado por aquele teste.

    Esse comportamento é declarado pelo parâmetro scope que por padrão recebe o
    valor 'function', indicando que antes de cada função de teste, essa fixure é
    executada. Logo, decorar o método com @pytest.fixture é a mesma coisa de
    @pytest.fixture(scope='function'):

    Ex.:
        @pytest.fixture(scope='function')
        def usuario(self):
            return Usuario('Matheus')

    ---
    Porém, algumas vezes criar as fixtures podem ser custosas para o sistema. Vamos
    imaginar que temos uma conexão com o banco de dados. Abrir a conexão antes de
    cada teste é custoso. Neste caso, o que podemos fazer é abrir a conexão no
    começo do módulo de testes e só fechá-la ao final.

    Conexão com o banco de dados, com um serviço de e-mails, com um serviço externo,
    ou até mesmo, um objeto que tem um valor imutável. São exemplos de objetos que
    podemos criar uma única vez e ir reutilizando nos testes.

    Por exemplo, o objeto usuario não altera estado, ele é apenas passado no
    construtor do carrinho de compras. Ou seja, se quisermos, podemos alterar seu
    escopo, mas qual escopo colocar?

    Existem diversos escopos que a pytest disponibiliza para nós utilizarmos. Nesse
    caso, temos apenas uma classe de teste no módulo, o que é bem comum, logo,
    podemos fazer que esse objeto seja instanciado apenas uma vez na classe,
    podemos fazer isso, alterando o escopo para class:

        class TestCarrinhoDeCompras:

            @pytest.fixture(scope='class')
            def usuario(self):
                return Usuario('Matheus')

    Dessa forma, o objeto é instanciado uma única vez, logo que a classe de testes
    é instanciada, e sua instância é compartilhada com os métodos.

    É importante notar que como a instância é compartilhada entre os métodos, é
    importante tomar cuidado com efeitos colaterais. Por exemplo, se colocarmos
    o escopo do carrinho como class, apenas o primeiro teste que é executado passa,
    já que o carrinho está vazio, enquanto os outros testes falham.
    """
    # @pytest.fixture(scope='function')
    # @pytest.fixture
    @pytest.fixture(scope='class') # Instanciado 1x quando instanciado a classe
    def usuario(self):
        return Usuario('Matheus')

    @pytest.fixture
    def carrinho(self, usuario):
        return CarrinhoDeCompras(usuario)

    @pytest.fixture
    def celular(self):
        return ItemDoCarrinho('Celular', 2100.0, 1)

    @pytest.fixture
    def notebook(self):
        return ItemDoCarrinho('Notebook', 4500.0, 1)

    @pytest.fixture
    def caneta_qtd5(self):
        return ItemDoCarrinho('Caneta', 3.00, 5)

    # def test_deve_retornar_subtotal_dos_itens_no_carrinho(self):
    def test_deve_retornar_subtotal_dos_itens_no_carrinho(  # 3º
            self, usuario, carrinho, celular, notebook, caneta_qtd5
    ):
        # given (dado, entrada) ▼
        # usuario = Usuario('Matheus') # 1º
        # usuario = self.usuario  # 2º
        # carrinho = CarrinhoDeCompras(usuario)
        # celular = ItemDoCarrinho('Celular', 2100.0, 1)
        # notebook = ItemDoCarrinho('Notebook', 4500.0, 1)
        # caneta = ItemDoCarrinho('Caneta', 3.00, 5)

        carrinho.adiciona(celular)
        carrinho.adiciona(notebook)
        # carrinho.adiciona(caneta)
        carrinho.adiciona(caneta_qtd5)

        valor_esperado = 6603.0
        resultado = carrinho.subtotal() # when (quando, executar algo, ação)

        assert valor_esperado == resultado # Then-desfecho

    # def test_deve_retornar_quantidade_total_dos_itens_no_carrinho_quando_este_nao_tiver_desconto(self):
    def test_deve_retornar_quantidade_total_dos_itens_no_carrinho_quando_este_nao_tiver_desconto(
            self, usuario, carrinho, celular, notebook, caneta_qtd5
    ):
        # Giver ▼
        # usuario = Usuario('Matheus')
        # carrinho = CarrinhoDeCompras(usuario)
        # celular = ItemDoCarrinho('Celular', 2100.0, 1)
        # notebook = ItemDoCarrinho('Notebook', 4500.0, 1)
        # caneta = ItemDoCarrinho('Caneta', 3.00, 5)

        carrinho.adiciona(celular)
        carrinho.adiciona(notebook)
        # carrinho.adiciona(caneta)
        carrinho.adiciona(caneta_qtd5)

        valor_esperado = 7
        resultado = carrinho.total_itens() # when

        assert valor_esperado == resultado # Then

    # def test_deve_retornar_total_dos_itens_no_carrinho_quando_este_nao_tiver_desconto(self):
    def test_deve_retornar_total_dos_itens_no_carrinho_quando_este_nao_tiver_desconto(
            self, usuario, carrinho, celular, notebook, caneta_qtd5
    ):
        # Given
        usuario = Usuario('Matheus')
        carrinho = CarrinhoDeCompras(usuario)
        celular = ItemDoCarrinho('Celular', 2100.0, 1)
        notebook = ItemDoCarrinho('Notebook', 4500.0, 1)
        caneta = ItemDoCarrinho('Caneta', 3.00, 5)

        carrinho.adiciona(celular)
        carrinho.adiciona(notebook)
        # carrinho.adiciona(caneta)
        carrinho.adiciona(caneta_qtd5)

        valor_esperado = 6603.0

        carrinho.aplica_desconto() # When
        resultado = carrinho.total()

        assert valor_esperado == resultado # Then

    # def test_deve_aplicar_desconto_ao_subtotal_dos_itens_no_carrinho_quando_este_nao_tiver_desconto(self):
    def test_deve_aplicar_desconto_ao_subtotal_dos_itens_no_carrinho_quando_este_nao_tiver_desconto(
            self, usuario, carrinho, celular, notebook, caneta_qtd5
    ):
        usuario = Usuario('Matheus')
        carrinho = CarrinhoDeCompras(usuario)
        celular = ItemDoCarrinho('Celular', 2100.0, 1)
        notebook = ItemDoCarrinho('Notebook', 4500.0, 1)
        caneta = ItemDoCarrinho('Caneta', 3.00, 5)

        carrinho.adiciona(celular)
        carrinho.adiciona(notebook)
        # carrinho.adiciona(caneta)
        carrinho.adiciona(caneta_qtd5)

        valor_esperado = 6103.0

        carrinho.aplica_desconto(500) # When
        resultado = carrinho.total()

        assert valor_esperado == resultado # Then
