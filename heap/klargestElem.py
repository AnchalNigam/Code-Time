# # for largest, min heap is used which is by default implementtaion in python heapfy function
# def KLargestElem(nums, k):
#   import heapq
#   pq = nums[:k]     
#   heapq.heapify(pq)
  
#   for i in range(k, len(nums)):
#       heapq.heappush(pq, nums[i])      
#       heapq.heappop(pq)
      
#   return pq[0]

# time complexity -  as in heapify - log (k) - k is number of elem in heap..
# we are actually heapifying n elems so nlogk as k elems ka heap bana rhe
# so nlogk time and space as k ka heap ban rha hai so o(k)
class MinHeap:
    def __init__(self, nums):
        self.heap = nums
    def getParent(self, i):
      return int(abs(i-1)/2)
    def getLeftChild(self, i):
      return 2*i


    def swapElement(self, i, j):
      # print(i, j)
      self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    def print(self):
        print(self.heap)
    def addElement(self, elem):
        self.heap.append(elem)
        i = len(self.heap)-1
        parent = self.getParent(i)
        while(self.heap[i] < self.heap[parent]):
            print(i, parent)
            self.swapElement(i, parent)
            i = parent
            parent = self.getParent(parent)
            # print(parent, 'check')
    def heapify(self):
      print(self.heap)
      temp = self.heap
      self.heap = []
      for i in range(len(temp)):
        self.addElement(temp[i])
      print(self.heap, 'heap')
    

    # def heapify(self, i):
    #   # eg : [4,2,1,3]
    #   smallest = i
    #   l = 2 * i + 1
    #   r = 2 * i + 2
    #   n = len(self.heap)
    #   if l <  n and self.heap[i] > self.heap[l]:
    #     smallest = l

    #   if r < n and self.heap[smallest] > self.heap[r]:
    #     smallest = r

    #   # Swap and continue heapifying if root is not smallest
    #   if smallest != i:
    #       self.heap[i],  self.heap[smallest] =  self.heap[smallest],  self.heap[i]
    #       self.heapify(smallest)

    def removeElement(self, element): 
    # if heapqpop toh simple 0th elem remove kr do as for minheap, it rmeoved smallest elem and vice versa
        n = len(self.heap)
        for i in range(n):
          if self.heap[i] == element:
            break
        print(i, 'yes', n-1)
        self.swapElement(i, n-1)
        self.heap.pop()
        self.heapify()

      


class Solution:
    def findKthLargest(self, nums, k):
      pq = nums
      heapify = MinHeap(pq)
    
      # for i in range(len(nums)):
      #   heapify.addElement(nums[i])
      heapify.heapify()
      # heapify.print()
      print(pq, 'bhar lo')
      # for i in range(k, len(nums)):
      #   heapify.addElement(nums[i])
      #   print(pq)
      #   heapify.removeElement(pq[0])
      #   print(pq, 'remove')
      # print(pq)
      # return pq[0]
        
sol = Solution()
sol.findKthLargest([3,4,1,2,6], 4)
        
# n = [3,4,1,2,6]
# import heapq
# heapq.heapify(n)
# print(n)
  
# its a working code....expected in leetcode...in this way we can implemet heap..specially see
# heapify function - 
# https://www.programiz.com/dsa/priority-queue

