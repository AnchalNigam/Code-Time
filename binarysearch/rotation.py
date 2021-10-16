class Solution:
  def search(self, nums: List[int], target: int) -> int:
      def findPivot(A):
          low = 0 
          high = len(A)-1
          B = A[high]
          while low < high:
              mid = low + (high-low)//2
              if A[mid] < B:
                  high = mid
              else:
                  low = mid+1
          return high

      def findIdx(A, B, low, high):
          while low <= high:
              mid = low + (high-low)//2
              if A[mid] == B:
                  return mid
              elif A[mid] < B:
                  low = mid + 1
              else:
                  high = mid - 1
          return -1
      pivot = findPivot(nums)
      high = len(nums) - 1
      low = 0
      if(nums[pivot] <= target and target <= nums[high]):
          return findIdx(nums, target, pivot, high)
      else:
          return findIdx(nums, target, low, pivot-1)  

# in this, frst approach was to find pivit like from where rotation happend
# to find that i firslt check if mid < last elemeent means everything is going good
# meaning right half is in ascending order so make high to mid then again left part 
# if there is mid > a[high] means this is not following patter means answer lies in right part
# in this way we will find pivot. then after that we have to find where is this target..
# left part rotatn or right part rotatn, then index find

# relateble questn - minimum element in sorted array, no of times array rotated