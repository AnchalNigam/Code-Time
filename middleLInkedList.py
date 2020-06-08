import math
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
  def middleElement(self):
    temp = self.head
    numOfElements = 0
    while(temp):
      numOfElements += 1
      temp = temp.next
    counter = 0
    temp = self.head
    while(temp):
      if(counter == math.floor(numOfElements/2)):
        print(temp.data)
        break
      counter += 1
      temp = temp.next
  def middleElement2(self):
    fast_ptr  = self.head
    slow_ptr = self.head
    while(fast_ptr.next != None and fast_ptr.next.next != None):
      fast_ptr = fast_ptr.next.next
      slow_ptr = slow_ptr.next
    print(slow_ptr.data)


root = LinkedList()
root.push(Node(5))
root.push(Node(4))
root.push(Node(3))
root.push(Node(12))
root.push(Node(11))

root.middleElement2()