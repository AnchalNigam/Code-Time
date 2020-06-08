class Node: 
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def print_list(self):
    temp = self.head
    while (temp):
      print(temp.data)
      temp = temp.next



if __name__ == '__main__':
  linkedList = LinkedList()
  linkedList.head = Node(2)
  second = Node(3)
  third = Node(4)

  linkedList.head.next = second
  second.next = third

  linkedList.print_list()


