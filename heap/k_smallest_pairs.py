from heapq import *
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):            
                if len(heap) < k:
                    heappush(heap, (-(nums1[i]+nums2[j]), [nums1[i], nums2[j]]))
                else:
                    if -(nums1[i]+nums2[j]) > heap[0][0]:
                        heappop(heap)
                        heappush(heap, (-(nums1[i]+nums2[j]), [nums1[i], nums2[j]]))
                    else:
                        break
        result = []
        while heap:
            _, pair = heappop(heap)
            result.append(pair)
        return result
            
            
# unable to solve..but i found one thingthat i need to consider all pairs
# here in heapm, we are considering all elems, and pushing in heap till k and maintaining
# max heap..as we are intersted in minimum sum so if any sum that will come greater than i dont care 
 
# because greater ko entertain h nahi krna hai..if lesser ayega then we will entertain 
# as negate me we are playing so - me jyda aye toh enetrtain krna hai[just reverse kr dia because of
# geate conditn]..in this way sol build hua....time complexity - 0(n*m*logk)
# space - o(k) beause of heap of k size 