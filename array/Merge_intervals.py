# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        results = []
        idx = 0
        while idx < len(intervals) and intervals[idx].end < new_interval.start:
            results.append(intervals[idx])
            idx += 1
        merge_interval = new_interval
        while idx < len(intervals) and intervals[idx].start <= merge_interval.end:
            merge_interval.start = min(intervals[idx].start, merge_interval.start)
            merge_interval.end = max(intervals[idx].end, merge_interval.end)
            idx += 1
        results.append(merge_interval)

        while idx < len(intervals):
            results.append(intervals[idx])
            idx += 1
        return results
