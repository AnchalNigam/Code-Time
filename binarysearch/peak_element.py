def solve(A):
  n = len(A) -1
  peak = A[0]
  for idx in range(1, n):
    if A[idx] > A[idx+1] and A[idx] > A[idx-1]:
      peak = A[idx]
  if peak < A[n]:
    return A[n]
  return peak
A =  [5, 17, 100, 11]
print(solve(A))
# o(n)

# o(logn)
class Solution:
  def findPeakElement(self, nums: List[int]) -> int:
      low = 0
      high = len(nums)-1 
      if len(nums) == 1:
          return 0
      while low <= high:
          mid = low + ((high-low)//2)
          if(mid > 0 and mid < len(nums)-1):
              
              if nums[mid] >= nums[mid-1] and nums[mid] >= nums[mid+1]:
                  return mid
              elif nums[mid] > nums[mid-1]:
                  low = mid + 1
              else:
                  high = mid - 1
          elif mid == 0:
              if nums[mid] > nums[mid+1]:
                  return 0
              else:
                  return 1
          elif mid == len(nums) - 1:
              if nums[mid] > nums[mid-1]:
                  return  mid
              else:
                  return mid-1
              
                  
      return -1 

# recheck video https://www.youtube.com/watch?v=OINnBJTRrMU
# self explained - finding mid and if that fails so we find because of which it fails
# b/c of right element or left, if right, it means right could be peak so low = mid+1 else
# high and mid==0 and mid==len(nums) cases handled separately