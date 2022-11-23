from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasible(capacity):
            day = 1
            total = 0
            for weight in weights:
                total += weight
                if total > capacity:
                    day += 1
                    total = weight
            if day > days:
                return False
            return True
        low, high = max(weights), sum(weights)
        while low < high:
            mid = low + (high-low)//2
            if feasible(mid):
                high = mid
            else:
                low = mid+1
        return low