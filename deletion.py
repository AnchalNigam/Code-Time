class Node: 
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
  
  def push(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      new_node.next = self.head
      self.head = new_node 


  def append(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      temp = self.head
      while(temp.next):
        temp = temp.next
      temp.next = new_node

  def insertAfter(self, prev_node, data):
    if prev_node is None:
      return
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node

  def deleteNode(self, key):
    temp = self.head
    if temp.next is None:
      self.head = None
      return
    if temp.data == key:
      self.head = temp.next
      return
    while(temp.data != key):
      prev = temp
      temp = temp.next

    prev.next = temp.next
    temp = None

  def positionDeletion(self, position):
    temp = self.head
    if position == 0:
      self.head = temp.next
      return
    for i in range(position - 1):
      temp = temp.next
    temp.next = temp.next.next
  
  def allNodesDel(self):
    current = self.head 
    while current: 
      prev = current.next # move next node s
      del current.data 
      current = prev  

  def getData(self, position):
    temp = self.head
    for i in range(position - 1):
      temp = temp.next
    return temp.data

  def print_list(self):
    temp = self.head
    print(temp.data)
    # while (temp):
    #   # print(temp.data, end = " ")
    #   temp = temp.next



if __name__ == '__main__':
  llist = LinkedList()
 
  llist.append(8)
  llist.append(10)
  llist.insertAfter(llist.head, 16)
  llist.append(11)
  print(llist.getData(2))
  # llist.print_list()

 

