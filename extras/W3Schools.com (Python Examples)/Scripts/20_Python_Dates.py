#-------------------------------------------------------------
#                     Python Examples
#-------------------------------------------------------------
#                      Python Dates
#-------------------------------------------------------------

print("-----------------------------------------------")

# Import the datetime module and display the current date
import datetime
x = datetime.datetime.now()
print(x)
# 2024-07-12 11:16:56.321576

print("-----------------------------------------------")

# Return the year and name of weekday
import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))
# 2024
# Friday

print("-----------------------------------------------")

# Create a date object
import datetime
x = datetime.datetime(2020, 5, 17)
print(x)
# 2020-05-17 00:

print("-----------------------------------------------")

# The strftime() Method
import datetime
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))
# June

print("-----------------------------------------------")