from heapq import *
from collections import deque
from typing import List
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic = {}
        for task in tasks:
            dic[task] = dic.get(task, 0) + 1
        freqTasks = []
        for task, freq in dic.items():
            heappush(freqTasks,(-freq,task))
        waitList = deque()
        c = 0
        while len(freqTasks) != 0 or len(waitList) != 0:            
            if len(waitList) != 0 and waitList[0][1] == c:
                waitingTask = waitList.popleft()
                heappush(freqTasks,(waitingTask[0],waitingTask[2]))
            if len(freqTasks) != 0:
                freq, task = heappop(freqTasks)
                if freq+1 != 0:
                    waitList.append((freq+1, c+n+1, task))
            c += 1
        return c
                
        
# interstng question
# https://www.youtube.com/watch?v=s8p8ukTyA2I

# good intutive sol above described...
# u can say i solved half. i got stuck in how we can reduce the waiting list elem time when i picked 
# frst elem from queue as if i am picking frst elem that means mjhe har ka waiting time dec krna padega
# so ye j face kr rhe the isme wht above sol is doing i is storing the indices 
# where this elem can be processed. its maintaining one array(visualiztn just) of processing
# if a is proessing at 0 then n=2 k lie n =3 pe we can again process so that why we ae storig the
# processing index wehre we ca process it, if we can process it then we are pushing it to
# max heap and whoever freq is most we will pick it and process
# time complexity - as (n) time iteratn to find freq and n times we are popping the elem and pushing
#n+nlogn..
# space as we are using max heap
# The space complexity will be O(N), as in the worst case, we need to store all the ‘N’ tasks in the HashMap.