import heapq

# Max heapq
nums = [3,2,1,5]
numsNegate = [ -i for i in nums]
heapq.heapify(numsNegate)
numsPositive = [ -i for i in numsNegate]
print(numsPositive)


# min heap...by default min heap rhta hai

# heapq.heapify(nums)
# heapq.heappush(12)
# heapq.heappop(2)

# by default prioeriy queue bhi kehte h max heap ko

# heappush -
# This function is used to insert the element mentioned in its arguments into heap. The order is adjusted, so as heap structure is maintained.

# heappop-
#  This function is used to remove and return the smallest element from heap. The order is adjusted, so as heap structure is maintained.
# IMP- heappop me we remove smallest element in case of minheap(FOR MAz heap, remove largest). and after removing heap order maintain hta hai
