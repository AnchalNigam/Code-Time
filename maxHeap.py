class MaxHeap:
  def __init__(self):
    self.heap = []
  def get_parent(self, i):
    return int(abs(i-1)/2)
  def swapElement(self, elem1Index, elem2Index):
    self.heap[elem1Index], self.heap[elem2Index] = self.heap[elem2Index], self.heap[elem1Index]
  def addElement(self, element):
    self.heap.append(element)
    i = len(self.heap)-1
    while(self.heap[i] > self.heap[self.get_parent(i)]):
      print(i, self.get_parent(i)) 
      self.swapElement(i, self.get_parent(i))
      i = self.get_parent(i)
  def printHeap(self):
    for i in self.heap:
      print(i, end=" ")
heap = MaxHeap()
heap.addElement(45)
heap.addElement(99)
heap.addElement(100)
heap.addElement(63)
heap.addElement(35)
heap.addElement(29)
heap.addElement(120)
heap.addElement(96)
heap.addElement(34)
heap.addElement(76)
heap.addElement(89)
heap.addElement(71)

heap.printHeap()

