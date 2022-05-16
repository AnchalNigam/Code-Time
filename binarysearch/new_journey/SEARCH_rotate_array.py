class Solution:
    def search(self, nums, target: int) -> int:
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = low + ((high-low)//2)
            if nums[mid] == target: 
                return mid
            elif nums[mid] >= nums[low]:
                if target < nums[mid] and target >= nums[low]:
                    high = mid-1
                else:
                    low = mid+1
            else:
                if target > nums[mid] and target <= nums[high]:
                    low = mid+1
                else:
                    high = mid-1
        return -1
                    
                    
# could not solve
# main logic ehich i understood we are comparing both target and pivot section..if suppose there
# is mid element which is greater than nums[0] means ye increasing hai now check for target
# if target < nums[mid] and target >= nums[0] meaning wo left half me h hai
# same goes for right if nums[mid] < nums[0] then check for target if target > nums[mid]
# target < nums[high] meaning right hald me hga ..visualize using [5,1,3], [4,5,6,7,0,1,2]

# elaboratve idea
# We have an ascending array, which is rotated at some pivot.
# Let's call the rotation the inflection point. (IP)
# One characteristic the inflection point holds is: arr[IP] > arr[IP + 1] and arr[IP] > arr[IP - 1]
# So if we had an array like: [7, 8, 9, 0, 1, 2, 3, 4] the inflection point, IP would be the number 9.

# One thing we can see is that values until the IP are ascending. And values from IP + 1 until end are also ascending (binary search, wink, wink).
# Also the values from [0, IP] are always bigger than [IP + 1, n].

# intuition:
# We can perform a Binary Search.
# If A[mid] is bigger than A[left] we know the inflection point will be to the right of us, meaning values from a[left]...a[mid] are ascending.

# So if target is between that range we just cut our search space to the left.
# Otherwise go right.

# The other condition is that A[mid] is not bigger than A[left] meaning a[mid]...a[right] is ascending.
# In the same manner we can check if target is in that range and cut the search space correspondingly.