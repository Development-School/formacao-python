#-------------------------------------------------------------
#                     Python Examples
#-------------------------------------------------------------
#                      Python RegEx
#-------------------------------------------------------------

print("-----------------------------------------------")

# Search a string to see if it starts with "The" and ends with "Spain"
import re

#Check if the string starts with "The" and ends with "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")
# YES! We have a match!

print("-----------------------------------------------")

# Using the findall() function
import re

#Return a list containing every occurrence of "ai":
txt = "The rain in Spain"
x = re.findall("ai", txt)

print(x)
# ['ai', 'ai']

print("-----------------------------------------------")

# Using the search() function
import re
#         3
#      012▼
txt = "The rain in Spain"
# x = re.search("\s", txt) # Error
x = re.search(r"\s", txt)

print("The first white-space character is located in position:", x.start())
# The first white-space character is located in position: 3

print("-----------------------------------------------")

# Using the split() function
import re

#Split the string at every white-space character:
txt = "The rain in Spain"
# x = re.split("\s", txt) #Error
x = re.split(r"\s", txt)

print(x)
# ['The', 'rain', 'in', 'Spain']

print("-----------------------------------------------")

# Using the sub() function
import re

#Replace all white-space characters with the digit "_":
txt = "The rain in Spain"
x = re.sub("\s", "_", txt)

print(x)
# The9rain9in9Spain

print("-----------------------------------------------")