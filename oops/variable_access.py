class A():
  cost = 0
  def __init__(self) -> None:
    self.var = 0
  # list = []

a = A()
b = A()
print(a.var)

print(b.var)
0
A.var = 1
A.cost = 2
a.cost = 1
print(b.cost, a.cost, a.var, A.cost)

# one is class variable, other is instance variable...class variable is shared by all
# instances whereas instance var is shared by instance itself...see above here cost is
# class variable and self.var is instance variable...ab what suppose tmcost k value change 
# kr rhe h A.cost = 2 then it would be same for both instance a and b but as hmne a.cost
#krke value 1 kr dia toh a.cost = 1 hga bt bt A.cost = 2 h hga so yahn a.cost ek instance
# var hai and A.cost ek class var toh agr apko instance var use krna h within class, use
# A.cost whereas per instance wala use krna h toh a.cost
# another understanding -  this creates a class-level cost variable, 
# but this is distinct from any instance-level a.cost variable
class A:
    static = 1
    list = []


class B(A):
    pass


print(f"int {A.static}")  # get 1 correctly
print(f"int {B.static}")  # get 1 correctly

A.static = 5
print(f"int {A.static}")  # get 5 correctly
print(f"int {B.static}")  # get 5 correctly

B.static = 6
print(f"int {A.static}")  # expected 6, but get 5 incorrectly
print(f"int {B.static}")  # get 6 correctly

A.static = 7
print(f"int {A.static}")  # get 7 correctly
print(f"int {B.static}")  # get unchanged 6
# ye scenario inheritance me class var ka behaviour dekha rha hai..isme A.static 
# and B.static would be same because inheritance se pass hua h value....second case me
# A.static change kr dia toh ab wo dono me A B 5 h jaega because  
# If attribute does not exists in inherited class, Python start to look for it in parent class.
# B.static kia 6 matlb ab B me wo define kr dia toh wo apna static variable B maintain kr lia
# because you have explicitly define it now A.static has 5 and B.static 6
# now A.static kroge toh B.static 6 h rhega because python looks frst in
# actual class then goes to parent as actual class me statis k value 6 h toh parent me na jaega
# 