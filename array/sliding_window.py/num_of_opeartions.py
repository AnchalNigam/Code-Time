arr = [-1, 2]
arr.sort()
i = 0
flag = False
summation = [0]
def printSubArrays(arr, start, end): 
      
    # Stop if we have reached the end of the array     
    if end == len(arr): 
        return
      
    # Increment the end point and start from 0 
    elif start > end: 
        return printSubArrays(arr, 0, end + 1) 
          
    # Print the subarray and increment the starting 
    # point 
    else: 
        summation[0] += sum(arr[start:end + 1])
        return printSubArrays(arr, start + 1, end) 
while i < len(arr):
  j = (i+2) - 1
  print(i,j)
  while j < len(arr) and j >= i:
    if arr[j] < 0:
      arr[j] = -arr[j]
    else:
      flag = True
      break
    j -= 1
  if flag:
    break
  i += 2
printSubArrays(arr, 0, 0)

print(summation[0])