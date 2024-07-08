#-------------------------------------------------------------
#                     Python Examples
#-------------------------------------------------------------
#                      Python Arrays
#-------------------------------------------------------------

print("-----------------------------------------------")

# Create an array
cars = ["Ford", "Volvo", "BMW"]
print(cars)
# ['Ford', 'Volvo', 'BMW']

print("-----------------------------------------------")

# Access the elements of an array
cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print(x)
# Ford

print("-----------------------------------------------")

# Change the value of an array element
cars = ["Ford", "Volvo", "BMW"]
cars[0] = "Toyota"
print(cars)
# ['Toyota', 'Volvo', 'BMW']

print("-----------------------------------------------")

# Get the length of an array
cars = ["Ford", "Volvo", "BMW"]
x = len(cars)
print(x)
# 3

print("-----------------------------------------------")

# Loop through all elements of an array
cars = ["Ford", "Volvo", "BMW"]
for x in cars:
  print(x)
# Ford
# Volvo
# BMW

print("-----------------------------------------------")

# Add an element to an array
cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda")
print(cars)
# ['Ford', 'Volvo', 'BMW', 'Honda']

print("-----------------------------------------------")

# Remove an element from an array - Ex.: 01
cars = ["Ford", "Volvo", "BMW"]
cars.pop()
print(cars)
# ['Ford', 'Volvo']

print("-----------------------------------------------")

# Remove an element from an array - Ex.: 02
cars = ["Ford", "Volvo", "BMW"]
cars.pop(1)
print(cars)
# ['Ford', 'BMW']

print("-----------------------------------------------")