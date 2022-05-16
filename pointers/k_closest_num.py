import heapq
from typing import List
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        low = 0
        high = len(arr)-1
        while low <= high:
            if k == (high-low)+1:
                return arr[low:high+1]
            else:
                if abs(arr[low]-x) <= abs(arr[high]-x):
                    high = high-1
                else:
                    low = low+1
        return []
                
# time complexity is n ..worst case would be n else n-k i guess....wost caselike wo elem closest one
# ekdum last me hai then we have to make our window equal to k so low=low+1 toh approx n traveerse 
# kr rhe hai