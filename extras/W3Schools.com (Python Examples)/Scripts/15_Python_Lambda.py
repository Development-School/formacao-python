#-------------------------------------------------------------
#                     Python Examples
#-------------------------------------------------------------
#                      Python Lambda
#-------------------------------------------------------------

print("-----------------------------------------------")

# A lambda function that adds 10 to the number passed
# in as an argument
x = lambda a: a + 10
print(x(5))
# 15

print("-----------------------------------------------")

# A lambda function that multiplies argument a with
# argument b
x = lambda a, b: a * b
print(x(5, 6))
# 30

print("-----------------------------------------------")

# A lambda function that sums argument a, b, and c
x = lambda a, b, c: a + b + c
print(x(5, 6, 2))
# 13

print("-----------------------------------------------")

# By Lucas
x = lambda a, b: a + ' ama ' + b + '!'
print(x('Lucas', 'Karla'))

print("-----------------------------------------------")