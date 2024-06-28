#-------------------------------------------------------------
#                     Python Examples
#-------------------------------------------------------------
#                   Python Dictionaries
#-------------------------------------------------------------

print("-----------------------------------------------")

# Create a dictionary
thisdict =  {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

print("-----------------------------------------------")

# Access the items of a dictionary
thisdict =  {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)
# Mustang

print("-----------------------------------------------")

# Change the value of a specific item in a dictionary
thisdict =  {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}

print()

thisdict.update({"model": "Ranger"})
print(thisdict)
# {'brand': 'Ford', 'model': 'Ranger', 'year': 2018}

print()
thisdict.update(brand='Toyota', model='Corolla', year='2016')
print(thisdict)
# {'brand': 'Toyota', 'model': 'Corolla', 'year': '2016'}

print("-----------------------------------------------")

# Print all key names in a dictionary, one by one
thisdict =  {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict: # Compactado ▼
  print(x)
# brand
# model
# year

print()

for k, v in thisdict.items(): # Descompactado ▼
  print(k, ' : ', v)
# brand
# model
# year

print("-----------------------------------------------")

# Print all values in a dictionary, one by one
thisdict =  {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])
# Ford
# Mustang
# 1964

print()

for x in thisdict:
  print(x, thisdict[x])
# Ford
# Mustang
# 1964

print("-----------------------------------------------")

# Using the values() function to return values of a dictionary
thisdict =  {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)
# Ford
# Mustang
# 1964

print("-----------------------------------------------")

# Loop through both keys an values, by using the items() function
thisdict =  {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)
# brand Ford
# model Mustang
# year 1964

print("-----------------------------------------------")

# Check if a key exists
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

# Yes, 'model' is one of the keys in the thisdict dictionary

print("-----------------------------------------------")

# Get the length of a dictionary
thisdict =  {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(len(thisdict))
# 3

print("-----------------------------------------------")

# Add an item to a dictionary
thisdict =  {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

print()

thisdict.update({"Creator": "Henry Ford"}) # Atenção, o "update()" adiciona um item caso não exista
print(thisdict)

print("-----------------------------------------------")

# Remove an item from a dictionary
thisdict =  {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
# {'brand': 'Ford', 'year': 1964}

print("-----------------------------------------------")

# Empty a dictionary
thisdict =  {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
# {}

print("-----------------------------------------------")

# Using the dict() constructor to create a dictionary
thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

print("-----------------------------------------------")