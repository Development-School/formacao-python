# Quick examples of convert list to set

# Initialize list
lists = [5, 2, 3, 4, 3, 5, 4, 6]
print(type(lists))
print(lists)
print("---")

# Example 1: Convert the list to a set
# Using set()
myset = set(lists)
print(type(myset))
print(myset)
print("---")
# Example 2: Convert list to set
# Using for loop
myset = set()
for item in lists:
    myset.add(item)
print(type(myset))
print(myset)
print("---")

# Example 3: Convert list to set
# Using set comprehension
myset = {item for item in lists}
print(type(myset))
print(myset)
print("---")

# Example 4: Convert list to set
# Using dict.fromkeys() method
myset = set(dict.fromkeys(lists))
print(type(myset))
print(myset)
