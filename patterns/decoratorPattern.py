# from abc import abstractmethod, ABC
# from lib2to3.pytree import Base
# not optimal way
# class BaseCharge(ABC):
#   def __init__(self, cost):
#     self.cost = cost
#   def get_cost(self):
#     return self.cost
#   def set_cost(self, cost):
#     self.cost = cost

# class RoomServiceCharge(BaseCharge):
#   def __init__(self, cost, baseCharge):
#     self.cost = cost
#     self.baseCharge = baseCharge
#   def get_cost(self):
#     self.baseCharge.set_cost(self.baseCharge.get_cost()+self.cost)
#     return self.baseCharge.get_cost()

# class OtherCharge(BaseCharge):
#   def __init__(self, cost, baseCharge):
#     self.cost = cost
#     self.baseCharge = baseCharge
#   def get_cost(self):
#     self.baseCharge.set_cost(self.baseCharge.get_cost()+self.cost)
#     return self.baseCharge.get_cost()


# a = BaseCharge(40)
# b = RoomServiceCharge(50, a)
# c = OtherCharge(50, a)

# print(b.get_cost())
# # print(b.get_cost())
# print(c.get_cost())
# print(c.get_cost())
# print(b.get_cost())
# x = RoomServiceCharge(10, a)
# print(x.get_cost())

# here scene is u are using diff costing and add each every charges..jahan diff combos ate h
# whn decorator pattern ata hai ab yahn scene ye hua ki agr apko 
# basecharge 

from abc import abstractmethod, ABC
from lib2to3.pytree import Base

class BaseCharge(ABC):
  def __init__(self, cost):
    self.cost = cost
  def get_cost(self):
    return self.cost
# is a relationship(inheritace)
class RoomServiceCharge(BaseCharge):
  def __init__(self, cost, baseCharge):
    self.cost = cost
    # has a relationship
    self.baseCharge = baseCharge
  def get_cost(self):
    return self.baseCharge.get_cost()+self.cost

class OtherCharge(BaseCharge):
  def __init__(self, cost, baseCharge):
    self.cost = cost
    self.baseCharge = baseCharge
  def get_cost(self):
    return self.baseCharge.get_cost()+self.cost


a = BaseCharge(40)
b = RoomServiceCharge(50, a)
c = OtherCharge(50, a)

x =  RoomServiceCharge(50, OtherCharge(50, OtherCharge(50, RoomServiceCharge(50, RoomServiceCharge(50, a)))))
print(x.get_cost())

# this is decorator pattern where multiple combo can be catered using just passing
# combos like roomservicecharge k upar other charges lagao ya esperesso+capuchino, american+capichino
# any kind of combo can be achieved just passing their instance and end me calling getcost function
# herre wrapping up and building new obj again and again is main funda..pehle sroomservice ka obj abanaya
# fr us ibj k roomservice me pass kia then ye total obj bhja othercharge me and so on

# above wale approach me we are actually mutating base class cos var by passing again and again a 
# object which is not actually a decorator pattern u can say....