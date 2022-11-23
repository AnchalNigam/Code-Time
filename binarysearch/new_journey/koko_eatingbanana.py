from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
       
        def feasible(capacity):
            # print(capacity)
            hour = 0
            total = 0
            for banana in piles:
                if banana <= capacity:
                    hour += 1
                else:
                    # print(math.ceil(banana/capacity), banana, banana/capacity)
                    hour += (math.ceil(banana/capacity))
            #     print(hour, banana)   
            # print(capacity, hour, h)
            if hour <= h:
                return True
            
            return False
     
        low = 1
        high = max(piles)
        while low < high:
            mid = low + (high-low)//2
            if feasible(mid):
                high = mid
            else:
                low = mid+1
        return low

# general template Isme dekho binary search aise hua ki sbse pehle hme ye dekhna h ki
#  isne pucha min weight mns hme ye pta krna h j possible values h skte h usme s min 
# kaise nikale toh agr hm har values k try kre and dekhe whether this much weight is 
# feasible 
# within d days or not then us bases pe we can set left 
# right(weights)...if its not possible mns weight aur badhao agr
#  feasible h toh converge kro kahin isse chota bi possible h kya so upar wale template 
# me feasible function me bs test kro adjacent elems k le lekr weights dekhna hai and days