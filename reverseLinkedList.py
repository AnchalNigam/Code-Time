# confidence boost

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
  
  def push(self, node):
    if self.head == None:
      self.head = node
    else:
      temp = self.head
      while(temp.next):
        temp = temp.next
      temp.next = node

  def print(self):
    temp = self.head
    while(temp):
      print(temp.data)
      temp = temp.next
  def reverse(self):
    prev = None
    current = self.head
    while(current):
      temp = current.next
      current.next = prev
      prev = current
      current = temp
    self.head = prev
  
  def isCircular(self):
    temp = self.head
    isCircular = False
    while(True):
      if temp.next == self.head:
        isCircular = True
        break
      if(temp.next is None):
        isCircular = False
        break
      temp = temp.next
    print(isCircular) 


root = LinkedList()
root.push(Node(5))
root.push(Node(4))
root.push(Node(3))
root.push(Node(12))
root.push(Node(11))

# root.reverse()
root.print()
root.isCircular()


