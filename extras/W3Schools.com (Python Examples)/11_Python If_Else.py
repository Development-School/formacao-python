#-------------------------------------------------------------
#                     Python Examples
#-------------------------------------------------------------
#                    Python If ... Else
#-------------------------------------------------------------

print("-----------------------------------------------")

# The if statement
a = 33
b = 200
if b > a:
  print("b is greater than a")
# b is greater than a

print("-----------------------------------------------")

# The elif statement
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
# a and b are equal

print("-----------------------------------------------")

# The else statement
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
# a is greater than b

print("-----------------------------------------------")

# Short hand if
a = 200
b = 33
if a > b: print("a is greater than b")
# a is greater than b

print("-----------------------------------------------")

# Short hand if ... else
a = 2
b = 330
print("A") if a > b else print("B")
# B

print("-----------------------------------------------")

# The and keyword
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
# Both conditions are True

print("-----------------------------------------------")

# The or keyword
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
# At least one of the conditions is True

print("-----------------------------------------------")