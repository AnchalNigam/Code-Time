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

  def reverse(self):
    current = self.head
    prev = None
    while(current):
      next = current.next
      current.next = prev
      prev = current
      current = next
    self.head = prev

  def reverse2(self,B,C):
    count = 1
    temp = self.head
    prev = None
    
    if C-B < 1:
        return A
    if B == 1:
      first = temp

    while(temp.next):
      if count == (B-1):
          first = temp
          temp = temp.next
      elif count >= B and count <= C:
          if count == B:
              firstNode = temp
          if count == C:
              lastNode = temp
              last = lastNode.next
          nextNode = temp.next
          temp.next = prev
          prev = temp
          temp = nextNode
      else:
          temp = temp.next
      count += 1
    if B == 1:
      self.head = lastNode
      firstNode.next = last
    else:
      first.next = lastNode
      firstNode.next = last

  def subtract_list(self):
    elements = []
    temp = self.head
    while(temp):
        elements.append(temp.data)
        temp = temp.next
    temp = self.head
    print(elements, '++')
    i = 0
    n = len(elements)//2
    while(i < n):
      temp.data = elements.pop() - temp.data
      i += 1
      temp = temp.next
        
    

  def print_list(self):
    temp = self.head
    while (temp):
      print(temp.data, end = " ")
      temp = temp.next



if __name__ == '__main__':
  llist = LinkedList()
 
  llist.append(1)
  llist.append(2)
  llist.append(3)
  llist.append(4)
  llist.append(5)

  # llist.print_list()
  # llist.insertAfter(llist.head, 16)
  # llist.reverse2(2,4)
  # llist.reverse()  # llist.reverse2(2,3)
  llist.subtract_list()
  llist.print_list()


 

