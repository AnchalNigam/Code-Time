arr = [1,2,3]
n = len(arr)
for j in range(n):
  arr[j] = arr[j] - 1
 
for idx in range(n):
  arr[(arr[idx]%n)] += n
print(arr)
for idx in range(n):
  print(arr[idx]//n, end="")

# explanation - once you iterate over array, first make it 0th index like 0 to n hai then make 
# 0 to n-1 by subtractng as array is 0th index. 
# second step is - for every occurence of that particular index means suppose 2 is occured the
# it means on 2nd index, your value will be updated so add n. for every occurence of 2 add n
# it will tell you 2 occurence, and for original value at that index, you know reminder would be
#  the original value of that index. so reminder is basically original value and divison by n is 
# actual one
# def majorityElement(A, N):
#       #Your code here
#       for idx in range(len(A)):
#         A[idx] = A[idx]-1
#       for idx in range(len(A)):
#           A[(A[idx]%N)] += N
#       print(A)
#       for idx in range(len(A)):
#           if (A[idx]//N) > N//2:
#               return A[idx]//N
#       return -1
# arr = [1, 13]
# N = len(arr)
# print(majorityElement(arr, N ))
# here if any element comes then we add +n in it so wo jiitne bar hga element utne bar +n hg
# so end me quotient will give freq and hm +n k sath jo us index me element h wo track rhe
# use bhi add kr rhe hai ar uska module matlb wo number get h gya j actual us index me tha before
# manipulating that array. so, in this way freq aa jaega
# o(n) , o(1) space above complexity