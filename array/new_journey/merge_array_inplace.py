def mergeArrayInPlace(m,n,nums1,nums2):
  i = m - 1
  j = n - 1
  k = (m + n) - 1
  while i >= 0 and j >= 0:
    if nums1[i] > nums2[j]:
      nums1[k] = nums1[i]
      k -= 1
      i -= 1
    else:
      nums1[k] = nums2[j]
      j -= 1
      k -= 1
  print(i, j, k, nums1)
  while j >= 0:
    nums1[k] = nums2[j] 
    j -= 1
    k -= 1

nums1 = [4,5,6,0,0,0]
m = 3
nums2 = [1,2,3]
n = 3  
print(mergeArrayInPlace(m,n,nums1,nums2))
print(nums1)