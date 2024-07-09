#-------------------------------------------------------------
#                     Python Examples
#-------------------------------------------------------------
#                Python Classes and Objects
#-------------------------------------------------------------

print("-----------------------------------------------")

# Create a class
class MyClass:
  x = 5

print(MyClass)
# <class '__main__.MyClass'>

print(MyClass.x) # 5

print()

print(dir(MyClass))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__',
# '__eq__', '__format__', '__ge__', '__getattribute__',
# '__getstate__', '__gt__', '__hash__', '__init__',
# '__init_subclass__', '__le__', '__lt__', '__module__',
# '__ne__', '__new__', '__reduce__', '__reduce_ex__',
# '__repr__', '__setattr__', '__sizeof__', '__str__',
# '__subclasshook__', '__weakref__', 'x']
print()
print(vars(MyClass))
# {'__module__': '__main__', 'x': 5,
# '__dict__': <attribute '__dict__' of 'MyClass' objects>,
# '__weakref__': <attribute '__weakref__' of 'MyClass' objects>,
# '__doc__': None}

print("-----------------------------------------------")

# Create an object
class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)
# 5

print("-----------------------------------------------")

# The __init__ () Function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)
print(p1.name)
print(p1.age)
# John
# 36

print("-----------------------------------------------")

# Create object methods
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
# Hello my name is John

print("-----------------------------------------------")

# The self parameter
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age
  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
# Hello my name is John

print("-----------------------------------------------")

# Modify object properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name + " and i have {} years old.".format(self.age))

p1 = Person("John", 36)

p1.age = 40
p1.myfunc()
print(p1.age)
# Hello my name is John and i have 40 years old.
# 40

print("-----------------------------------------------")

# Delete object properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
del p1.age
# print(p1.age)
"""Traceback (most recent call last):
  File "demo_class7.py", line 13, in <module>
    print(p1.age)
AttributeError: 'Person' object has no attribute 'age'"""

print("-----------------------------------------------")

# Delete an object
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
del p1
# print(p1)
"""Traceback (most recent call last):
  File "demo_class8.py", line 13, in <module>
    print(p1)
NameError: 'p1' is not defined"""

print("-----------------------------------------------")