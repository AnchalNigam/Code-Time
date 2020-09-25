a = [ 14, 24, 18, 46, 55, 53, 82, 18, 101, 20, 78, 35, 68, 9, 16, 93, 101, 85, 81, 28, 78 ]
# a.sort()
# print(a)
# a = [20,10,11,12,13]
# without memoization
#  def maxSequence(a,lastSeq,index):
#     if len(a) == 1:
#         return 1
#     if index >= len(a):
#         return 0
#     m1 = 0
#     if lastSeq < a[index]:
#         m1 = 1 + maxSequence(a, a[index],index+1)
#     m2 = maxSequence(a, lastSeq, index+1)
#     return max(m1,m2)
# print(maxSequence(nums, float('-inf'), 0))
# with memoization
# dic = {}
# def maxSequence(lastSeq,index):
#   if index >= len(a):
#     return 0
#   if (index,lastSeq) in dic:
#     return dic[(index, lastSeq)]
#   m1 = 0
#   if lastSeq < a[index]:
#     m1 = 1 + maxSequence(a[index],index+1)
#   m2 = maxSequence(lastSeq, index+1)
#   dic[(index, lastSeq)] = max(m1, m2)
#   return dic[(index, lastSeq)]
#   # return max(m1,m2)

# print(maxSequence(0,0))