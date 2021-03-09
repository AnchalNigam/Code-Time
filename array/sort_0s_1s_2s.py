#  def sort012(self,arr,n):
#         # code here
#         l = 0
#         m = 0
#         h = n-1
#         while(m<=h):
#             if arr[m] == 0:
#                 arr[l], arr[m] = arr[m], arr[l]
#                 l += 1
#                 m += 1
#             elif arr[m] == 1:
#                 m += 1
#             else:
#                 arr[h], arr[m] = arr[m], arr[h]
#                 h -= 1


l = 0
m = 0

arr = [0, 1, 2, 0, 1, 2]
h = len(arr)-1
while m <= h:
  if arr[m] == 0:
    arr[l], arr[m] = arr[m], arr[l]
    l += 1
    m += 1
  elif arr[m] == 1:
    m += 1
  else:
    arr[m], arr[h] = arr[h], arr[m]
    h -= 1

print(arr)