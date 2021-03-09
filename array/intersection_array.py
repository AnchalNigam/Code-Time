# ist way
# def intersect(nums1, nums2):
#   dic = {}
#   res = []
#   for idx in range(len(nums1)):
#     startIdx = -1
#     if nums1[idx] in dic:
#       startIdx = dic[nums1[idx]][len(dic[nums1[idx]])-1]
#     for idx2 in range(startIdx+1, len(nums2)):
#       if nums1[idx] == nums2[idx2]:
#         res.append(nums1[idx])
#         if nums1[idx] in dic:
#           dic[nums1[idx]].append(idx2)
#         else:
#           dic[nums1[idx]] = [idx2]
            
#         break
#   return res

# print(intersect([1,2,2,1],
# [2]))

# 2nd way
def intersect(nums1, nums2):
  nums1, nums2 = sorted(nums1), sorted(nums2)
  i = j = 0
  res = []
  print(nums1, nums2)
  while i < len(nums1) and j < len(nums2):
    print(i, j, 'test')
    if nums1[i] == nums2[j]:
      res.append(nums1[i])
      i += 1
      j += 1
    elif nums1[i] > nums2[j]:
      j += 1
    else:
      i += 1
  return res

print(intersect([4,9,5],
[9,4,9,8,4]))

# [4, 5, 9] [4, 4, 8, 9, 9]