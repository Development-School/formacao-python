
from package.culinaria import Receita

r = Receita(autor="nico", tempo_preparo="??")

print(r.autor)
print(r.tempo_preparo)

r.autor = "marco"
print(r.autor)
