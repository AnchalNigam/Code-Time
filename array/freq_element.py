arr = [1,2,3]
n = len(arr)
for j in range(n):
  arr[j] = arr[j] - 1
 
for idx in range(n):
  arr[(arr[idx]%n)] += n
print(arr)
for idx in range(n):
  print(arr[idx]//n, end="")

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