
class Aluno:
 def __init__(self,nome,nota_1,nota_2):
    self.nome  = nome
    self.nota_1= nota_1
    self.nota_2= nota_2
    # self.media= 0.0
    self.media= float(0.0)

 def get_media(self):
     # self.media = (self.nota_1+self.nota_2)/2.0
     return (self.nota_1+self.nota_2)/2.0

 def imprimir(self):
     print(f"{self.nome}, você tirou {self.nota_1} "
           f"na primeira nota e {self.nota_2} "
           # f"na sua segunda nota, sua média ficou {self.media}.")
           f"na sua segunda nota, sua média ficou {self.get_media()}.")

 def resultado(self):
     # if self.media>=6.0:
     if self.get_media()>=6.0:
         print("Você foi aprovado")
     else:
         print("Você foi reprovado")

# nome_aluno1 = input("Digite seu nome: ")
# nota1_aluno1 = float(input("Digite sua primeira nota: "))
# nota2_aluno1 = float(input("Digite sua segunda nota: "))
nome_aluno1 = 'Lucas'
nota1_aluno1 = float(7.2)
nota2_aluno1 = float(7.2)

geral_aluno1 = Aluno(nome_aluno1, nota1_aluno1, nota2_aluno1)
# media_aluno1 = geral_aluno1.media()
media_aluno1 = geral_aluno1.get_media()

print(f'Média do aluno: {media_aluno1}')

geral_aluno1.imprimir()
geral_aluno1.resultado()