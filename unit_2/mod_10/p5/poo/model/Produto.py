
class Produto: # Classe Abstrata
  def __init__(self, nome, preco, quantidade):
    self.nome = nome
    self.preco = preco
    self.quantidade = quantidade

  def mostrar_info(self):
    print(f"Nome: {self.nome}")
    print(f"Preço: R${self.preco}")
    print(f"Quantidade: {self.quantidade}")

  def mostrar_valor_total_estoque(self):
    valor_total = self.preco * self.quantidade
    print(f"O valor total de estoque deste produto é R${round(valor_total, 2)}")
