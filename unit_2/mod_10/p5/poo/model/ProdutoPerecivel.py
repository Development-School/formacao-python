from unit_2.mod_10.p5.poo.model.Produto import Produto

class ProdutoPerecivel(Produto): # Herança, Herdando atributos e comportamento da classe mãe Produto

  # Adição de um novo atributo "data_validade"
  def __init__(self, nome, preco, quantidade, data_validade):
    super().__init__(nome, preco, quantidade)
    self.data_validade = data_validade

  # Novo comportamento de mostrar a validade do Produto.
  def mostrar_validade(self):
    print(f"O produto vence no dia {self.data_validade}")

  def mostrar_info(self): # Exemplo de Poliformismo (sobrecarga de métodos), herdando da classe mãe porém com comportamento diferente
    super().mostrar_info()
    print("="*30)
    print(f"Esse produto é perecível!")
    print("="*30)
