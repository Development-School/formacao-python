#-------------------------------------------------------------
#                     Python Examples
#-------------------------------------------------------------
#                      Python Tuples
#-------------------------------------------------------------

print("-----------------------------------------------")

# Create a tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)
# ('apple', 'banana', 'cherry')

print("-----------------------------------------------")

# Access tuple items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
# banana

print("-----------------------------------------------")

# Change tuple values
thistuple = ("apple", "banana", "cherry")
print(thistuple)
# ('apple', 'banana', 'cherry')

# thistuple[1] = "blackcurrant" # TypeError: 'tuple' object does not support item assignment
# Tuplas são imutáveis
# Uma solução seria converter para lista, alterar, e depois converter novamente para tuple

thistuple = list(thistuple)
thistuple[1] = "blackcurrant"
thistuple = tuple(thistuple)

# the value is still the same:
print(thistuple)


print("-----------------------------------------------")

# Loop through a tuple
thistuple = ("apple", "banana", "cherry")

for x in thistuple:
  print(x)

# apple
# banana
# cherry

print("-----------------------------------------------")

# Check if a tuple item exists
thistuple = ("apple", "banana", "cherry")

if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

# Yes, 'apple' is in the fruits tuple

print("-----------------------------------------------")

# Get the length of a tuple
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
# 3

print("-----------------------------------------------")

# Delete a tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)
# ('apple', 'banana', 'cherry')

# del thistuple
# Traceback (most recent call last):
#   File "demo_tuple_del.py", line 3, in <module>
#     print(thistuple) #this will raise an error because the tuple no longer exists
# NameError: name 'thistuple' is not defined

# Tuplas são imutáveis
# Uma solução seria re-declarar a tupla

thistuple = ()
print(thistuple) #this will raise an error because the tuple no longer exists
# ()

print("-----------------------------------------------")

# Using the tuple() constructor to create a tuple
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)
# ('apple', 'banana', 'cherry')

print(type(thistuple))
# <class 'tuple'>

print("-----------------------------------------------")