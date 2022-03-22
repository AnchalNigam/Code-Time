from ctypes.wintypes import PINT
import heapq


class MaxHeap:
  def __init__(self):
    self.heap = []
  def getParent(self, i):
    return (i-1)//2

  def swapElement(self, i, j):
    # print(i, j)
    self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
  def print(self):
    print(self.heap)
  def addElement(self, elem):
    self.heap.append(elem)
    i = len(self.heap)-1
    parent = self.getParent(i)
    while(self.heap[i] > self.heap[parent]):
      # print(i, parent)
      self.swapElement(i, parent)
      parent = self.getParent(parent)

  def removeElement(self, element):
    n = len(self.heap)
    for i in range(n):
      if self.heap[i] == element:
        break
    self.swapElement(i, n-1)
    self.heap.pop()
    self.heapify(0)
  def addElemv2(self, i):
      largest = i
      l = 2 * i + 1
      r = 2 * i + 2
      n = len(self.heap)
      if l <  n and self.heap[i] > self.heap[l]:
        largest = l

      if r < n and self.heap[largest] > self.heap[r]:
        largest = r

      # Swap and continue heapifying if root is not smallest
      if largest != i:
          self.heap[i],  self.heap[largest] =  self.heap[largest],  self.heap[i]
          self.addElemv2(largest)




  
class MinHeap:
  def __init__(self):
    self.heap = []
  def getParent(self, i):
    return (i-1)//2
  def print(self):
    print(self.heap)
  def swapElement(self, i, j):
    self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
  def addElement(self, element):
    self.heap.append(element)
    i = len(self.heap)-1
    parent = self.getParent(i)
    while(self.heap[i] < self.heap[parent]):
      self.swapElement(i, parent)
      parent = self.getParent(parent)
  def addElemv2(self, i):
      smallest = i
      l = 2 * i + 1
      r = 2 * i + 2
      n = len(self.heap)
      if l <  n and self.heap[i] > self.heap[l]:
        smallest = l

      if r < n and self.heap[smallest] > self.heap[r]:
        smallest = r

      # Swap and continue heapifying if root is not smallest
      if smallest != i:
          self.heap[i],  self.heap[smallest] =  self.heap[smallest],  self.heap[i]
          self.addElemv2(smallest)


heapify = MaxHeap()
# heapify = MinHeap()

heapify.addElement(3)
heapify.addElement(3)
heapify.addElement(1)
heapify.addElement(5)

heapify.print()
# heapify.removeElement(50)
# heapify.print()




# timecomplexiy is insertion, deletion - o(logn) because per //2 parent parent check mns by hald half we are going above
# n, n/2, n/4...1 = 1
# n / 2^k = 1
# k = log(base2)n

# to add elem, just check last and then get parent then compare and so on
# for deleteiom , find the elem and then swap with last element, pop the last elem and heapify again
# max heap is said as priority queue....not so good but can take reference from here 
# https://www.programiz.com/dsa/priority-queue