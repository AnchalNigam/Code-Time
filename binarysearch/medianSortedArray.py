# not optimised way
# def median(A, B):
#     B = list(B)
#     A = list(A)
#     C = []
#     i = 0
#     j = 0
#     k = 0
#     while i < len(A) and j < len(B):
#       if A[i] <= B[j]:
#         C.append(A[i])
#         i += 1
#       else:
#         C.append(B[j])
#         j += 1
#       k += 1
#     while i < len(A):
#       C.append(A[i])
#       i += 1
#       k += 1
#     while j < len(B):
#       C.append(B[j])
#       j += 1
#       k += 1
#     if(len(C) == 1) :
#         return C[0]
#     print(C)
#     if len(C)%2 == 0:
#         mid = len(C)//2
#         return (C[mid]+C[mid-1])/2
#     else:
#         return C[len(C)//2]
# A = [0, 23 ]
# B = []
# print(median(A, B))

# optimized way

def median(A, B):
  if(len(A) > len()):
    return median(B, A)
  arr1 = list(A)
  arr2 = list(B)
  low = 0
  n1 = len(arr1)
  n2 = len(arr2)
  high = len(arr1)
 
  while(low <= high):
    cut1 = (high + low) // 2
    cut2 = ((n1 + n2)//2) - cut1
    l1 = float('-inf') if cut1 == 0 else arr1[cut1-1]
    l2 =  float('-inf') if cut2 == 0 else arr2[cut2-1]
    
    r1 = float('inf') if cut1 == n1 else arr1[cut1]
    r2 = float('inf') if cut2 == n2 else arr2[cut2]
    if(l1 <= r2 and l2 <= r1):
      if((n1+n2) % 2 == 0):
        return (max(l1, l2) + min(r1, r2)) /2 
      else:
        return max(l1, l2)
    elif(l1 > r2):
      high = cut1 - 1
    else:
      low = cut1 + 1
  return 0.0

A = [ -43, -25, -18, -15, -10, 9, 39, 40 ]
B = [ -2 ]
print(median(A, B), 'jii')
      

# here firstly we are trying to make left and right half as our answer can be taken out 
# if we have found left half, if even then left half contains more element than right like
# 9 elements then 5 in left and 4 in right. we start by taking half of shorter array
# as we know that max elements that we can take from array is their length, firstly we find shorter
# array and high define on length of shorter array thats why if(len(A)) one logic. after that
# we make cut1 means how many elements from arr1 then remaining from arr2. (n1+n2+1)/2 we have
# taken because total array will (arr1+arr2)/2-cut1 then left half banega but +1 in n1+n2 we do because
# we want more elem in left half than right half in case of unqual divison (even)
# then l1 is last element in left half, if no left half elem then -inf similarly for right part
# then gave result, for better explanation - https://www.youtube.com/watch?v=NTop3VTjmxk&list=RDCMUCJskGeByzRRSvmOyZOz61ig&index=9
    
