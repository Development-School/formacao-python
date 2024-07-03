

arquivo = open("palavras.txt", "w") # Escrever/Sobrescrever um arquivo
arquivo
# Ps.: Vai salvar o arquivo automaticamente no mesmo lugar deste content.py
# Ps²: Caso não informe o modificador "w" o python automaticamente atribuirá como leitura "r"

arquivo.write("banana")
# 6

arquivo.write("melancia")
# 8

arquivo.close()

arquivo = open("palavras.txt", "a") # Adicionar ao arquivo

arquivo.write("morango\n")
# 8

arquivo.write("manga\n")
# 6

arquivo.close()

# bananamelanciamorango
# manga

# Editar Manualmente no arquivo
# banana
# melancia
# morango
# manga