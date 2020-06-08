class Node: 
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
  def array_list(self, arr):
    for i in arr:
      new_Node = Node(i)
      if (self.head is None):
        self.head = new_Node
      else:
        temp = self.head
        while(temp.next):
          temp = temp.next
        temp.next = new_Node

  def print_list(self):
    temp = self.head
    while (temp):
      print(temp.data, '-->', end = " ")
      temp = temp.next



if __name__ == '__main__':
  arr = [2, 6, 8, 10]
  llist = LinkedList()

  llist.array_list(arr)
  llist.print_list()

 

