
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
      node.next = self.head
    else:
      temp = self.head
      node.next = self.head
      while(temp.next != self.head):
        temp = temp.next
      temp.next = node
      node.next = self.head

  def print(self):
    temp = self.head
    while(temp.next != self.head):
      print(temp.data)
      temp = temp.next
    print(temp.data)
 
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

root.print()
root.isCircular()

