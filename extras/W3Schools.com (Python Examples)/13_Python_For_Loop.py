#-------------------------------------------------------------
#                     Python Examples
#-------------------------------------------------------------
#                     Python For Loop
#-------------------------------------------------------------

print("-----------------------------------------------")

# The for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
# apple
# banana
# cherry

print("-----------------------------------------------")

# Loop through a string
for x in "banana":
  print(x)
# b
# a
# n
# a
# n
# a

print("-----------------------------------------------")

# Using the break statement in a for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
# apple
# banana

print("-----------------------------------------------")

# Using the continue statement in a for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    continue
# apple
# banana
# cherry

print("-----------------------------------------------")

# Using the range() function in a for loop
for x in range(6):
  print(x)
# 0
# 1
# 2
# 3
# 4
# 5

print("-----------------------------------------------")

# Else in for loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")
# 0
# 1
# 2
# 3
# 4
# 5
# Finally finished!

print("-----------------------------------------------")

# Nested for loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)
# red apple
# red banana
# red cherry
# big apple
# big banana
# big cherry
# tasty apple
# tasty banana
# tasty cherry

print("-----------------------------------------------")