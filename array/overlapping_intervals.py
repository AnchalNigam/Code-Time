def overlapping(intervals):
  intervals = sorted(intervals, key = lambda x: x[1])
  tempEnd, count = float('-inf'), 0
  for start, end in intervals:
      if start >= tempEnd:
          tempEnd = end
      else:
          count += 1
  return count


                
#             The heuristic is: always pick the interval with the earliest end time. Then you can get the maximal number of non-overlapping intervals. (or minimal number to remove).
# This is because, the interval with the earliest end time produces the maximal capacity to hold rest intervals.
# Therefore, we can sort interval by ending time and key track of current earliest end time. Once next interval's start time is earlier than current end time, then we have to remove one interval.
#  Otherwise, we update earliest end time.