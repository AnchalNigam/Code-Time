# Python program to
# demonstrate protected members

# Creating a base class
class Base:
  def __init__(self):
    self.__b = 4
    self.c = 11
		# Protected member
    self._a = 2
  def check(self):
    print(self.c, self.__b, self._a)

# Creating a derived class
class Derived(Base):
  def __init__(self):
    Base.__init__(self)
    print("Calling protected member of base class: ",
      self._a)
    # Modify the protected variable:
    self._a = 3
    self.c = 21
    print("Calling modified protected member outside class: ",
      self._a)


obj1 = Derived()

obj2 = Base()
print(obj2.check())
obj2.c = 12
obj2._a = 4
obj2.__b = 5
# changed value shown for public, protected vars, not for private one
print(obj2.check()) 
# obj1._a = 5
# Calling protected member
# Can be accessed but should not be done due to convention
print("Accessing protected member of obj1: ", obj1._a) 
# out of above is 3

# Accessing the protected variable outside
print("Accessing protected member of obj2: ", obj2._a)
# out of above is 2 see ye class base apna varibale and methods rkhte hai
# derived class apna rkhe h toh j modify kroge apne apne tak dono rkhnge..whi scene h yhan