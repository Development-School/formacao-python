
#-------------------------------------------------------------
#                     Python Examples
#-------------------------------------------------------------
#                     Python Strings
#-------------------------------------------------------------

print("-----------------------------------------------")

# Get the character at position 1 of a string
a = "Hello, World!"
print(a[1]) # e

print("-----------------------------------------------")

# Substring. Get the characters from position 2 to position 5 (not included)
b = "Hello, World!"
print(b[2:5]) # llo

print("-----------------------------------------------")

# Remove whitespace from the beginning or at the end of a string
a = " Hello, World! "
print(a.strip()) # Hello, World!

print("-----------------------------------------------")

# Return the length of a string
a = "Hello, World!"
print(len(a)) # 13

print("-----------------------------------------------")

# Convert a string to lower case
a = "Hello, World!"
print(a.lower()) # hello, world!

print("-----------------------------------------------")

# Convert a string to upper case
a = "Hello, World!"
print(a.upper()) # HELLO, WORLD!

print("-----------------------------------------------")

# Replace a string with another string
a = "Hello, World!"
print(a.replace("H", "J")) # Jello, World!

print("-----------------------------------------------")

# Split a string into substrings
a = "Hello, World!"
print(a) # Hello, World!

b = a.split()
print(b) # ['Hello,', 'World!']

b = a.split(",") # Dividir a string
print(b) # ['Hello', ' World!']

print("-----------------------------------------------")