#-------------------------------------------------------------
#                     Python Examples
#-------------------------------------------------------------
#                     Python Functions
#-------------------------------------------------------------

print("-----------------------------------------------")

# Create and call a function
def my_function():
  print("Hello from a function")

my_function()
# Hello from a function

print("-----------------------------------------------")

# Function parameters
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
# Emil Refsnes
# Tobias Refsnes
# Linus Refsnes

print("-----------------------------------------------")

# Default parameter value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
# I am from Sweden
# I am from India
# I am from Norway
# I am from Brazil

print("-----------------------------------------------")

# Let a function return a value
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
# 15
# 25
# 45

print("-----------------------------------------------")

# Recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results ▼")
tri_recursion(6)
# Recursion Example Results
# 1
# 3
# 6
# 10
# 15
# 21

print("-----------------------------------------------")