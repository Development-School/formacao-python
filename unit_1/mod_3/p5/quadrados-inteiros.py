# -------------------------------------------------------------------- #
# 09. Preenchendo uma lista com os quadrados de números inteiros
# -------------------------------------------------------------------- #


inteiros = [1,3,4,5,7,8]
print(inteiros)

quadrados = [index*index for index in inteiros]
print(quadrados)
# [1, 9, 16, 25, 49, 64]
