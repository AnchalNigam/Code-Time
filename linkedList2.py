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
  linkedList.head = Node(1)
  second = Node(3)
  third = Node(4)
  fourth = Node(5)

  linkedList.head.next = second
  second.next = third
  third.next = fourth

  linkedList.print_list()


