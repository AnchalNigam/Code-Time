from typing import List


def maxSum(arr, n):
    # Write your code here
    # arr.sort()
    summation = 0
    print(arr)
    for i in range(len(arr)):
        summation += arr[i] * i
    return summation
arr = [1, -2, 3, -4, 5]

# print(maxSum(arr, 6))

# 28
# 11
# 6 12
# 9 13
# 6 14
# 9 12
# 8 14
# 5 10
# 8 11
# 6 10
# 6 13
# 7 10
# 6 11
def modifiedLudo(connections : List[List[int]], length: int):
    # Write your code here
    connections.sort(key = lambda x: ((x[1]-6)))
    roll = 0
    
    n = len(connections)
    n2 = n
    for i in range(n):
      if connections[i][1] > length:
        n2 = i-1
        break

    print(n2, 'checkkk', connections)
    temp2 = connections[n2-1][0]-1
    if temp2%6== 0:
        roll = temp2//6
    else:
        roll = temp2//6+1
    temp = (length - connections[n2-1][1])
    reminder = temp%6
    quotient = temp//6
#     print(reminder, quotient)
    if reminder == 0:
        return quotient+roll
    return quotient+roll+1

# 53
# 12
# 33 39
# 2 15
# 9 33
# 34 39
# 47 48
# 31 51
# 2 12
# 45 51
# 48 50
# 22 42
# 4 36
# 3 36
arr = [[33,39], [2,15], [9,33], [34,39],[47,48],[31,51],[2,12],[45,51],[48,50],[22,42],[4,36],[3,36]]


print(modifiedLudo(arr, 53))