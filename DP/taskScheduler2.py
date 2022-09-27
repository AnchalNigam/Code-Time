
from typing import List


class Solution:

    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        waitList = {}
        c = 0
        ans = 0
        for task in tasks:
            # print(c, waitList)
        
            if task in waitList:
                c = max(waitList[task], c)
                
            waitList[task] = c+space+1
            c += 1
            
        return c
# nice questn here scene is order me krna hai jis order me tasks hai
# agr task waitlist nhi h toh bhai jo uska hga next day calc kro c+space+1
# then agr waitList me h see kis din hne chahye kaam if time jyda h mns curr day pehle h
# break lena padega so just update curr to jis din wo kaam krna hai
# else whi rhne do mns chota h waitList[task] so normal logic waitList[task]=c+space+1
# c+=1 

                
            
            
        
        