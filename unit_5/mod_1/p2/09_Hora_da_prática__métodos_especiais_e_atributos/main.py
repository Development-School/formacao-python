


# 1) Crie uma classe chamada Veiculo com um método
# abstrato chamado ligar.

# model/Veiculo.py

# 3)Crie uma nova classe chamada Carro que herda da classe Veiculo.

# model/Carro.py

# 5) Em um arquivo chamado main.py, importe a classe Carro.

# from model.Veiculo import Veiculo
# from veiculo import Carro
from model.Carro import Carro

# 6) No arquivo main.py, instancie três objetos da classe
# Carro com diferentes características, como marca, modelo e cor.

print("-----------------------------------------------")

carro1 = Carro(marca="Ford", modelo="Focus", cor="Preto")
carro2 = Carro(marca="Chevrolet", modelo="Cruze", cor="Prata")
carro3 = Carro(marca="Honda", modelo="Civic", cor="Vermelho")

print(f"Carro 1: {carro1.marca} {carro1.modelo}, Cor: {carro1.cor}")
print(f"Carro 2: {carro2.marca} {carro2.modelo}, Cor: {carro2.cor}")
print(f"Carro 3: {carro3.marca} {carro3.modelo}, Cor: {carro3.cor}")

print("-----------------------------------------------")