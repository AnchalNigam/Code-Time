
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

  def deleteNode(self, key):
    temp = self.head
    if self.head is None:
      return None
    elif temp.next is None:
      self.head = None
      return
    elif temp.data == key:
      self.head = temp.next
      return
    prev = temp
    while(temp):
      if temp.data == key:
        break
      prev = temp
      temp = temp.next
    prev.next = temp.next
    temp = None


    
  def removeDuplicates(self):
    temp = self.head
    dic = {}
    while(temp):
      if temp.data not in dic:
        dic[temp.data] = 1
      temp = temp.next
    uniqueData = list(dic.keys())
    uniqueData = uniqueData[::-1]
    self.head = None
    for i in uniqueData:
      newNode = Node(i)
      self.push(newNode)
  
  def removeDuplicates2(self):
    temp = self.head
    dic = {}
    while(temp):
      if temp.data not in dic:
        dic[temp.data] = 1
      else:
        dic[temp.data] += 1
      temp = temp.next
    temp = self.head
    while(temp):
      if dic[temp.data] > 1:
        self.deleteNode(temp.data)
        dic[temp.data] -= 1
      temp = temp.next


        



root = LinkedList()
root.push(Node(5))
root.push(Node(4))
root.push(Node(5))
root.push(Node(3))
root.push(Node(3))
root.push(Node(3))
root.push(Node(12))
root.push(Node(4))
root.push(Node(11))
root.push(Node(12))
root.push(Node(11))



root.removeDuplicates2()
root.print()


