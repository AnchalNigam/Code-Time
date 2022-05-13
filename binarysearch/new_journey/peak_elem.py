def findPeakElement(nums):
    low = 0
    high = len(nums)-1   
    while low < high-1:
        mid = low + ((high-low)//2)
        if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
            return mid
        elif nums[mid] > nums[mid+1]:
            high = mid-1
        else:
            low = mid+1
    return low if nums[low] >= nums[high] else high

# here very smart approach.i could not solve prob because i was trying to compare with prev value
# but here what they have done is to compare with neighbours ..if it satisfies then simply returning mid
# if not satisfying like nums[mid] > nums[mid+1] meaning aisa h skta hai ki mid se pehle h kahin 
# ye satisfy kr skta hai toh converge ar kro left side me thats why high = mid-1 and again findout
# in this converge krke, we have found our mid...man le last line tak aa jaye toh 
# low if nums[low] >= nums[high] else high


# visualize this eg for better undestanding- [1,6,5,4,3,2,1]

# complexity - o(logn)