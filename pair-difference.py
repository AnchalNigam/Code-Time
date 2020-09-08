# one way o(n)

def solve(self, A, B):
  dic = {}
  for idx, value in enumerate(A):
      if value not in dic:
          dic[abs(value+B)] = idx
      else:
          return 1
  return 0

# other way
# 1. sort the array 
# then use below function
def findPair(arr,n): 
  
  size = len(arr) 

  # Initialize positions of two elements 
  i,j = 0,1

  # Search for a pair 
  while i < size and j < size: 

      if i != j and arr[j]-arr[i] == n: 
          print "Pair found (",arr[i],",",arr[j],")"
          return True

      elif arr[j] - arr[i] < n: 
          j+=1
      else: 
          i+=1
  print "No pair found"
  return False