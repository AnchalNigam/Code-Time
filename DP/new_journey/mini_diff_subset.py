def subset_sum(arr, sum):
  dp = [[-1 for idx in range(sum+1)] for idx2 in range(len(arr)+1)]
  for i in range(len(arr)+1):
    for j in range(sum+1):
      if i == 0:
        dp[i][j] = False
      if j == 0:
        dp[i][j] = True
  for i in range(1, len(arr)+1):
    for j in range(1, sum+1):
      if arr[i-1] <= j:
        dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
      else:
         dp[i][j] = dp[i-1][j]
  return dp

def minDifference(arr):
  summation = 0
  for idx in range(len(arr)):
    summation += arr[idx]

  dp_matrix = subset_sum(arr, summation)
  minimum = float('inf')
  for i in range(summation//2, -1, -1):
      if dp_matrix[len(arr)][i] == True:
        minimum = min(minimum, summation-(2*i))
  return minimum
arr = [1, 6, 5, 11]
# arr = [5, 6, 6, 5, 7, 4, 7, 6]
print(minDifference(arr))

# beautiful and hard. basically here the main moto is we have to find diff bwtween two susbset 
# to make it minimum. this is quite similar like allocate books[binary seacrh] but unlike binary
# search, we can take elem in contiguous manner. anything can pick. so here what we do
# we take whatever the possible values of min, obvio 1 to sum of arr element
#  but each value can't be possible in subsets like [1,2,7] with sum 4 is not feasible
# so first prepare table of true false, what are possible values for 3 element, 1 possible
# 2,3,4,5,5,6 what is possible. after getting this, we know s2=range-s1 so s2-s1=range-2s1
# so min will be calculate till half as s1 we are thinking as smaller. 24 to 25 line number
# is basically for calculatng min. for better understand, 
# https://www.youtube.com/watch?v=-GtpxG6l_Mc&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=10 





