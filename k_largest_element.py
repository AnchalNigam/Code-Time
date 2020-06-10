# //Running time - 0.64s
# log2𝑛. As others have mentioned, the built-in sorting algorithm of Python uses a special version of merge sort, called Timsort, which runs in  𝑛log2𝑛  time.

T = int(input())
from heapq import heappop, heappush, heapify 
def getKLargestElements(arr,k):
  arr = [value*-1 for value in arr]
  heapify(arr)
  arr = [value*-1 for value in arr]
  print(arr, '++')

# def getKLargestElements(arr, k):
#   arr.sort(reverse=True)
  return arr[:k]
for t in range(T):
  k = list(map(int, input().split()))[1]
  arr = list(map(int, input().split()))
  print(getKLargestElements(arr, k))

