#-------------------------------------------------------------
#                     Python Examples
#-------------------------------------------------------------
#                      Python Lists
#-------------------------------------------------------------

print("-----------------------------------------------")

# Create a list
thislist = ["apple", "banana", "cherry"]
print(thislist)
# ['apple', 'banana', 'cherry']

print("-----------------------------------------------")

# Access list items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
# banana

print("-----------------------------------------------")

# Change the value of a list item
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"

print(thislist)
# ['apple', 'blackcurrant', 'cherry']

print("-----------------------------------------------")

# Loop through a list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
# apple
# banana
# cherry

print("-----------------------------------------------")

# Check if a list item exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
# Yes, 'apple' is in the fruits list

thislist = ["apple", "banana", "cherry"]
fruit = "orange"
if fruit in thislist:
    print(f"Yes, '{fruit}' is in the fruits list")
else:
    print(f"Não, ',{fruit}' is not the fruits list")
# Não, ',orange' is not the fruits list

print("-----------------------------------------------")

# Get the length of a list
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
# 3

print("-----------------------------------------------")

# Add an item to the end of a list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
# ['apple', 'banana', 'cherry', 'orange']

print("-----------------------------------------------")

# Add an item at a specified index
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
# ['apple', 'orange', 'banana', 'cherry']

print("-----------------------------------------------")

# Remove an item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
# ['apple', 'cherry']

print("-----------------------------------------------")

# Remove the last item
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
# ['apple', 'banana']

print("-----------------------------------------------")

# Remove an item at a specified index
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
# ['banana', 'cherry']

print("-----------------------------------------------")

# Empty a list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
# []

print("-----------------------------------------------")

# Using the list() constructor to make a list
print(type(("apple", "banana", "cherry")))
# <class 'tuple'>

thislist = list(("apple", "banana", "cherry"))
print(thislist)
# ['apple', 'banana', 'cherry']
print(type(thislist))
# <class 'list'>

print("-----------------------------------------------")