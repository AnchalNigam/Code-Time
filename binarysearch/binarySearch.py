arr = list(map(int,input().split()))
k = int(input())
def binarySearch(arr, k):
  low = 0
  high = len(arr) - 1
  while low <= high:
    mid = low + (high-low)//2
    if arr[mid] == k:
      print(mid)
      break
    elif arr[mid] < k:
      low = mid+1
    else:
      high = mid-1
  return -1
binarySearch(arr,k)


# why low+high/2 not because every integer type is having some holding capacity so if high
# is more then overflow occurs that your integrer does not hold and give unexpected result
# Here is an example, suppose you had a very big array of size 2,000,000,000 and 10 (10^9 + 10) and the left index was at 2,000,000,000 and the right index was at 2,000,000,000 + 1.

# By using lo + hi will sum upto 2,000,000,000 + 2,000,000,001 = 4,000,000,001. Since the max value of an integer is 2,147,483,647. So you won't get 4,000,000,000 + 1, you will get an integer overflow.

# But low + ((high - low) / 2) will work. 2,000,000,000 + ((2,000,000,001 - 2,000,000,000) / 2) =  2,000,000,000