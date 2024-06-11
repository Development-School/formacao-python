
print('a' * 75) # Repetir caractere ou string
# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

print("-----------------------------------------------")

str = 'StackOverflow'
print ((str[:13] + ' ') * 5)
# StackOverflow StackOverflow StackOverflow StackOverflow StackOverflow

print("-----------------------------------------------")

a = 'StackOverflow'
print (a * 5)
# StackOverflowStackOverflowStackOverflowStackOverflowStackOverflow

print("-----------------------------------------------")

letter_count_dict = {'a': 1, 'b': 3, 'c': 2, 'd': 1}
for key, value in letter_count_dict.items():
    print(key * value, end="")

print()
# abbbccd

print("-----------------------------------------------")