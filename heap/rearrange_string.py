from heapq import *
from collections import deque
class Solution:
    def reorganizeString(self, s: str) -> str:
        dic = {}
        for char in s:
            dic[char] = dic.get(char, 0) + 1
        chars = []
        for char, freq in dic.items():
            heappush(chars, (-freq, char))
        waitList = []
        c = 0
        res = ""
        while chars or waitList:
            if waitList and waitList[0][1] == c:
                waitingElem = waitList.pop(0)
                heappush(chars, (waitingElem[0], waitingElem[2]))
            
            if chars:
                freq, char = heappop(chars)
                res += char
                if (freq+1) != 0:
                    waitList.append((freq+1, c+2, char))
            else:
                res = ""
                break

            c += 1
                
        return res
                
        
# i did it by own..main thing is i used concept of task scheuler here
# here waiting time is just n = 1 and same questn
# ifWAITING time mns ivalid string and  send "" . see how heap is beautiful...here occurence 
# jiske jyda h usko priority dene the thats maxheap use hua and wait ka concept lagaya
# time complexity same - n+nlogn...space is o(n) because of maxheap and worsst case me n h hga
# when all elem are distnct