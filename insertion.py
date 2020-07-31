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


  def print_list(self):
    temp = self.head
    while (temp):
      print(temp.data, end = " ")
      temp = temp.next



if __name__ == '__main__':
  llist = LinkedList()
 
  llist.append(8)
  llist.append(10)
  llist.insertAfter(llist.head, 16)
  llist.print_list()

 

