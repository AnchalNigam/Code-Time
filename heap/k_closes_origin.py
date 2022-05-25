import heapq
from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)
        pq = []
        for i in range(n):
            # print(pq)
            if len(pq) < k:
                dis =  -(points[i][0]**2 + points[i][1]**2)
                heapq.heappush(pq, [dis, points[i][0], points[i][1]])
            else:  
                dis1 = (points[i][0])**2 + (points[i][1])**2
                dis2 = (pq[0][1])**2 + (pq[0][2])**2
                if dis1 < dis2:
                    heapq.heappop(pq)
                    heapq.heappush(pq, [-dis1, points[i][0], points[i][1]])           
        return [[x,y] for _, x, y in pq]


# i solved it semi ..idea was right but not fully solved by own ..looked into sol...
# main idea is use heap...as we know we have to find those poits which are close to
# (0,0)..so we will frstly make max heap means max wala j oriigin se that is on top
# so now will go to next elem then will check the distance of that pooints from
# origin and heap frst elem then agr point k dis kam hga then will push it and pop
# pop will remove max distance from heap...here we have aintained dis for 
# maintaining heap...eg suppose 5 7 9 10 8 are members...for 3 size max heap..
# heap will have at top 9 and childs 5 7...then 10 comes, checking 10 with
# 9 and found its not min than 9 so ignore and mpve to next elem..next elem is 8 which
# is less than 9 and obvio all others elem in heap is smaller than 9 and coming is also
# less then will pop 9 and inseert 7 so bsic idea of max heap is used but dis is used to
# calculate above theory not points coordinate....interestng ques
# time complexity is n elems traverse but heap k size ka tha toh nlogk hga
