#-------------------------------------------------------------
#                     Python Examples
#-------------------------------------------------------------
#                      Python Math
#-------------------------------------------------------------

print("-----------------------------------------------")

# Find the lowest and highest value in an iterable
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x) # 5
print(y) # 25

print("-----------------------------------------------")

# Return the absolute value of a number
x = abs(-7.25)

print(x) # 7.25

print("-----------------------------------------------")

# Return the value of x to the power of y (xy)
x = pow(4, 3) # 4 x 4 x 4
y = pow(2, 3) # 2 x 2 x 2
z = pow(5, 2) # 5 x 5

print(x) # 64
print(y) # 8
print(z) # 25

print("-----------------------------------------------")

# Return the square root of a number
import math
x = math.sqrt(64)
y = math.sqrt(9)
z = math.sqrt(4)

#print(x) # 8.0

print(int(x)) # 8
print(int(y)) # 3
print(int(z)) # 2

print("-----------------------------------------------")

# Round a number upwards and downwards to its nearest integer

#Import math library
import math

#Round a number upward to its nearest integer
x = math.ceil(1.4)
print(x) # 2

#Round a number downward to its nearest integer
y = math.floor(1.4)
print(y) # 1

print("-----------------------------------------------")

# Return the value of PI
import math

x = math.pi
print(x) # 3.141592653589793
print()

print(x.__round__(2)) # 3.14
print(round(x, 2)) # 3.14
print()

print("{:.2f}".format(x)) # 3.14
print()

# import decimal
# print("{}".format(decimal.Decimal(x).quantize(decimal.Decimal("0.00"), rounding=decimal.ROUND_HALF_UP))) # 3.14

from decimal import Decimal, ROUND_HALF_UP
print("{}".format(Decimal(x).quantize(Decimal("0.00"), rounding=ROUND_HALF_UP))) # 3.14

print("-----------------------------------------------")