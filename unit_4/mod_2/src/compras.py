import functools


class Usuario:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f'{self.nome}'

class CarrinhoDeCompras:
    def __init__(self, usuario):
        self.usuario = usuario
        self.item_Do_Carrinho = []
        self.desconto = 0

    def adiciona(self, novo_item_Do_Carrinho):
        self.item_Do_Carrinho.append(novo_item_Do_Carrinho)

    def lista_produto(self):
        for item in self.item_Do_Carrinho:
            print(f'Produto: {item.nome} Valor: R${item.valor} '
                  f'Quantidade: R$ {item.quantidade}')

    def subtotal(self):
        total = 0
        for item in self.item_Do_Carrinho:
            total += item.valor

        return total

    def total(self):
        return (self.subtotal() - self.desconto)

    # Sobrecarga (Não existe em python... utilizamos de artifício)▼
    def aplica_desconto(self, desconto=None):
        if desconto is None:
            self.desconto = 0
        else:
            self.desconto = desconto

    def total_itens(self):
        total = 0
        for item in self.item_Do_Carrinho:
            total += item.quantidade

        return total

class ItemDoCarrinho:
    def __init__(self, nome, valor, quantidade):
        self.nome = nome
        self.valor = valor
        self.quantidade = quantidade
