#-------------------------------------------------------------
#                     Python Examples
#-------------------------------------------------------------
#                    Python While Loop
#-------------------------------------------------------------

print("-----------------------------------------------")

# The while loop
i = 1
while i < 6:
  print(i)
  i += 1
# 1
# 2
# 3
# 4
# 5

print("-----------------------------------------------")

# Using the break statement in a while loop
i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1
# 1
# 2
# 3

print("-----------------------------------------------")

# Using the continue statement in a while loop
i = 1
while i < 6:
  print(i)
  i += 1
  if i == 3:
    continue
# Note that number 3 is missing in the result
# 1
# 2
# 4
# 5

print("-----------------------------------------------")
