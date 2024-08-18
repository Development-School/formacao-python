#-------------------------------------------------------------
#                     Python Examples
#-------------------------------------------------------------
#                    Python Try Except
#-------------------------------------------------------------

print("-----------------------------------------------")

# When an error occurs, print a message
#The try block will generate an error, because x is not defined:
# x = 5
try:
  print(x)
except:
  print("An exception occurred")

# An exception occurred

print("-----------------------------------------------")

# Many exceptions
#The try block will generate a NameError, because x is not defined:
# x = 5
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

# Variable x is not defined

print("-----------------------------------------------")

# Use the else keyword to define a block of code to be executed if no errors were raised
#The try block does not raise any errors, so the else block is executed:
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

# Hello
# Nothing went wrong

print("-----------------------------------------------")

# Use the finally block to execute code regardless if the try block raises an error or not
#The finally block gets executed no matter if the try block raises any errors or not:
# x = 5
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

# Something went wrong
# The 'try except' is finished

print("-----------------------------------------------")