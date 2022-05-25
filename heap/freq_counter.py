import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        s = ''.join(sorted(s))
        heap = []
        prev = ""
        c = 0
        for i in range(len(s)):
            if prev == s[i]:
                c += 1
            else:
                if prev != "":                            
                    heapq.heappush(heap, (-c, prev))
                prev = s[i]
                c = 1
        heapq.heappush(heap, (-c, prev))
        # print(heap)
        result = ""
        while len(heap) > 0:
            popElem = heapq.heappop(heap)
            result += (popElem[1]*(popElem[0]*-1))
        return result
                
# i solved it by own..basic idea sort frst and then find freq of chars and push into heap(maxheap)
 # after maintaining heap, just pepare your res...
 # time complexity as sorting is done so o(nlogn) + n + mlogm + mlogm - sorting ka o(nlogn)
 # n for loop, heappush as its done for distinct elements say m so mlogm ..similarly heapop
  # obvio distinct elem ka h heap bana h toh mlogm
  # space is as heap using o(m), m distinct chars 
  # and in worst case if all chars are distinct then m logm bhi n logn h jaega so overall either
  # in best or worst, nlogn h rha hai because of initial sorting 
            
import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        heap = []
        dic = {}
        for char in s:
            if char not in dic:
                dic[char] = 1
            else:
                dic[char] += 1
        for char, freq in dic.items():
            heapq.heappush(heap, (-freq, char))
        result = ""
        # print(heap)
        while len(heap) > 0:
            popElem = heapq.heappop(heap)
            result += (popElem[1]*(popElem[0]*-1))
        return result
# this i saw someone else's sol, here basic idea is map maintain then heappush each freq elem
# time complexity - mainly heap ka scene hai dominant which is mlogm , for char traversal
# n ..major is mlogm and when all chars are distnct then nlogn but here big benefit is in
# avg and best case
# space - dic o(m)+o(m) - worst case would be o(n)+o(n) when all chars distnct


# keep in mind - priortztn me heaps use kro like here mjhe jyda freq wale elem k priorty dene the
# so i used heap
                
            
            
        