from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        i = 0
        result = []
        newI = intervals[0]
        result.append(newI)
        for j in range(1, len(intervals)):
            if intervals[j][0] <= newI[1]:
                # print(i, j)
                newI[1] = max(intervals[j][1], newI[1])
            else:   
                newI = intervals[j]
                result.append(newI)
              
        return result
                




