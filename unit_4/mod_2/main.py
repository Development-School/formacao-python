
from src.compras import *

print("-----------------------------------------------")

# Testando classe Usuario
usuario = Usuario('Matheus')
print(usuario)
# Matheus

print("-----------------------------------------------")

# Testando classe CarrinhoDeCompras
# Imprimindo usuário do carrinho de compras
carrinho = CarrinhoDeCompras(usuario)
print(carrinho.usuario)
# Matheus

# Testando se lista inicial do carrinho está vazia
print(carrinho.item_Do_Carrinho)
# []

print("-----------------------------------------------")

# Testando função para incluir produto/item no carrinho
celular = ItemDoCarrinho('Celular', 2100.0, 1)
notebook = ItemDoCarrinho('Notebook', 4500.0, 1)
caneta = ItemDoCarrinho('Caneta', 3.00, 5)

# Imprimindo itens declarados
print(celular.nome, celular.valor, celular.quantidade)
# Celular 2100.0 1

print(notebook.nome, notebook.valor, notebook.quantidade)


print(caneta.nome, caneta.valor, caneta.quantidade)

print("-----------------------------------------------")

# Testando função de adicionar itens ao carrinho
carrinho.adiciona(celular)
carrinho.adiciona(notebook)
carrinho.adiciona(caneta)
print(f'O {carrinho.usuario} possui a seguinte lista de '
      f'compras:')
# O Matheus possui a seguinte lista de compras:

carrinho.lista_produto()
# Produto: Celular Valor: R$2100.0
# Produto: Notebook Valor: R$4500.0
# Produto: Caneta Valor: R$3.0

print("-----------------------------------------------")

# Testando função de soma total dos produtos do carrinho
print(f'Soma total = {carrinho.subtotal()}')
# Soma total = 6603.0

print("-----------------------------------------------")

# Testando soma total de itens
print(f'Total de itens = {carrinho.total_itens()}')

print("-----------------------------------------------")

# Teste de desconto de valor
# Valor total.....: 6603.0
# Desconto de.....: 500
# Total esperado é: 6103

print(f'Valor total = R$: {carrinho.total()} | '
      f'Desconto de: R$ {carrinho.desconto}')
# Valor sem desconto: 6603.0

carrinho.aplica_desconto(500)
print(f'Valor total = R$: {carrinho.total()} | '
      f'Desconto de: R$ {carrinho.desconto}')
# 6103.0

print("-----------------------------------------------")

# Realizar agora os testes em "exemplo_test_classe_carrinho_de_compras.py"

r"""
============================= test session starts =============================
collecting ... collected 4 items

exemplo_test_classe_carrinho_de_compras.py::TestCarrinhoDeCompras::test_deve_retornar_subtotal_dos_itens_no_carrinho PASSED [ 25%]
exemplo_test_classe_carrinho_de_compras.py::TestCarrinhoDeCompras::test_deve_retornar_quantidade_total_dos_itens_no_carrinho_quando_este_nao_tiver_desconto PASSED [ 50%]
exemplo_test_classe_carrinho_de_compras.py::TestCarrinhoDeCompras::test_deve_retornar_total_dos_itens_no_carrinho_quando_este_nao_tiver_desconto PASSED [ 75%]
exemplo_test_classe_carrinho_de_compras.py::TestCarrinhoDeCompras::test_deve_aplicar_desconto_ao_subtotal_dos_itens_no_carrinho_quando_este_nao_tiver_desconto PASSED [100%]

============================== 4 passed in 0.02s ==============================
"""

print("-----------------------------------------------")