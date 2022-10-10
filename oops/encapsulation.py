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
# obj2.__b = 5
# print(obj2.__b)

# private variables gyan - 

# see if we try to access obj.__b it will give u attribiute error because provate variables
# are not accesible outisde the class whereas if you write line num 33 and then try 
# to print line 34 then it will print 5 (may be ye naya variable smjhta h and then keh deta 5 )
# but mota mota if you want to access private vars outside class , it will not be accessible
# to access orivate variable getter functn banao(eg check function) now we aare able to access
# private vars too...
# if you want to modfy private vars it will not be modified see line 34 (purane h value ayege __b
#  ki which is 4 so modfy bhi na hta private vars). tO MODIFY PRIVATE VARS
# use setter function
# changed value shown for public, protected vars, not for private one
print(obj2.check()) 

# protected member gyan-
# here its accessible inside clas ad subclass but here we can access protected 
# and modify outisde the class(see below 10 kr dia _a k ar wo hoyega bhi)
#  too because python allows that
# obj1._a = 5
# Calling protected member
# Can be accessed but should not be done due to convention
obj1._a = 10
print("Accessing protected member of obj1: ", obj1._a) 
# out of above is 3

# # Accessing the protected variable outside
# print("Accessing protected member of obj2: ", obj2._a)
# out of above is 2 see ye class base apna varibale and methods rkhte hai
# derived class apna rkhe h toh j modify kroge apne apne tak dono rkhnge..whi scene h yhan

# conslusion - 
# pblic vars access bhi hte, modify bhi inside class and subclass..
# private not access outside na h bahar se chang h skte, use getter settle for this
# potected - access bhi h rhe hai and modify bhi