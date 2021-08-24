 def merge(self, intervals):
        if(len(intervals) == 0 or len(intervals) == 1):
            return intervals
        intervals.sort(key=lambda x: x.start)
        results = []
        current = intervals[0]
        idx = 1
        while(idx < len(intervals)):
            if(current.end >= intervals[idx].start):
                current.start = min(current.start, intervals[idx].start)
                current.end = max(current.end, intervals[idx].end)
            else:
                results.append(current)
                current = intervals[idx]
            idx += 1
        results.append(current)
        return results