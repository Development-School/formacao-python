#-------------------------------------------------------------
#                     Python Examples
#-------------------------------------------------------------
#                     Python Iterators
#-------------------------------------------------------------

print("-----------------------------------------------")

# Return an iterator from a tuple
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
# print(next(myit)) # Error StopIteration
# apple
# banana
# cherry

print("-----------------------------------------------")

# Return an iterator from a string
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
# b
# a
# n
# a
# n
# a

print("-----------------------------------------------")

# Loop through an  iterator
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)
# apple
# banana
# cherry

print("-----------------------------------------------")

# Create an iterator
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
# 1
# 2
# 3
# 4
# 5

print("-----------------------------------------------")

# Stop iteration
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20

print("-----------------------------------------------")