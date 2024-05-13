# -------------------------------------------------------------------- #
# 07. is vs ==
# -------------------------------------------------------------------- #




print(0 == False)
# True

print(1 == True)
# True

print("" == False)
# False

print(bool(""))
# False

print(bool("") is False)
# True

print(None == False)
# False

print("-----------------------------------------------")

a = float('nan')
print('is -> {}'.format(a is a))
# is -> True
print('== -> {}'.format(a == a))
# == -> False