# question link, https://leetcode.com/discuss/interview-question/124554/Find-Max-Bandwidth/#:~:text=For%20n%20tv%20channels%2C%20given,time%2C%20bandwidth%2Dneeded%5D.&text=Ans%3A%2013%2C%20for%20time%20slot,%2C5%2C4%20bandwidth%20respectively.
# https://aaronice.gitbook.io/lintcode/sweep-line/meeting-rooms-ii
def solve(channels):
  from heapq import heappop, heappush
  channels.sort(key = lambda x: x[0])
  heap = []
  bandWidth = 0
  maxBandWidth = float('-inf')
  for show in channels:
    if not heap:
      bandWidth += show[2]
      heappush(heap, (show[1], show[2]))
      continue
    if heap[0][0] <= show[0]:
      _endTime, band = heappop(heap)
      maxBandWidth = max(maxBandWidth, bandWidth)
      bandWidth -= band
    bandWidth += show[2]
    heappush(heap, (show[1], show[2]))
  return maxBandWidth
    
channel = [[1,30, 2],[31,60, 4],[61,120, 3],
[1,20,2],[21,40,4],[41,60,5],[61,120,3],
[1,60,4],[61,120,4]]
print(solve(channel))

# def solve(meetings):
#   from heapq import heappop, heappush
#   meetings.sort(key = lambda x: x[0])
#   heap = []
#   minRooms = 0
#   for meeting in meetings:
#     if not heap:
#       heappush(heap, meeting[1])
#       continue
#     if heap[0] <= meeting[0]:
#       heappop(heap)
#     heappush(heap, meeting[1])
#   return len(heap)
    
# meetings = [[7,10],[2,4]]
# print(solve(meetings))


# amazon question - interestng could not solved but learnt that overlapping problems
# can be done using sorting or sorting/heap...here main logic is sort all channels
# acc tp their broadcast start time...ab j pehle shuru hnge pehle aa gye 
# now ab overlapping time janne k lie maintain heapp..jo pehle khatam h rha hai
# wo sbse upar then jo start sbse pehle hua uska start time agr jyda hai and equal h
# mns next show uske bad shuru h toh matlb overlapping nhi h so pop kr do heap me 
# j show pada h because its non overlapping ..then again push curr elem in heap
# now again check if thats greater(heap end time is lesser than next show start time or next
# show time is greater than heap end time)
# then again pop because again non overalping so time wale me non overapping aise dhundho