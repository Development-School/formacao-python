#-------------------------------------------------------------
#                     Python Examples
#-------------------------------------------------------------
#                      Python Sets
#-------------------------------------------------------------

print("-----------------------------------------------")

# Create a set
thisset = {"apple", "banana", "cherry"}
print(thisset)
# Note: the set list is unordered, meaning: the items will appear in a random order.
# Refresh this page to see the change in the result.
# {'banana', 'apple', 'cherry'}

print("-----------------------------------------------")

# Loop through a set
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
# banana
# apple
# cherry

print("-----------------------------------------------")

# Check if an item exists
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
# True

print("-----------------------------------------------")

# Add an item to a set
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
# {'orange', 'cherry', 'apple', 'banana'}

print("-----------------------------------------------")

# Add multiple items to a set
thisset = {"apple", "banana", "cherry"}
thisset.update(["orange", "mango", "grapes"])
print(thisset)
# {'apple', 'cherry', 'mango', 'banana', 'orange', 'grapes'}

print("-----------------------------------------------")

# Get the length of a set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))
# 3

print("-----------------------------------------------")

# Remove an item in a set
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
# {'cherry', 'apple'}

print("-----------------------------------------------")

# Remove an item in a set by using the discard() method
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
# {'cherry', 'apple'}

print("-----------------------------------------------")

# Remove the last item in a set by using the pop() method
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) #removed item
print(thisset) #the set after removal
# banana
# {'cherry', 'apple'}

print("-----------------------------------------------")

# Empty a set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
# set()

print("-----------------------------------------------")

# Delete a set
thisset = {"apple", "banana", "cherry"}
# del thisset
print(thisset) #this will raise an error because the set no longer exists
"""Traceback (most recent call last):
  File "demo_set_del.py", line 5, in <module>
    print(thisset) #this will raise an error because the set no longer exists
NameError: name 'thisset' is not defined"""

print("-----------------------------------------------")

# Using the set() constructor to create a set
thisset = set(("apple", "banana", "cherry"))
print(thisset)
# Note: the set list is unordered, so the result will display the items in a random order.
# {'apple', 'cherry', 'banana'}
print(type(thisset))
# <class 'set'>

print("-----------------------------------------------")