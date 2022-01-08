def minFallingPathSum(matrix):
  n = len(matrix)
  for i in range(1, n):
    for j in range(0, n):
      matrix[i][j] += min(matrix[i-1][j], matrix[i-1][max(0, j-1)], matrix[i-1][min(j+1, n-1)])

  # minVal = float('inf')
  # for i in range(n):
  #   minVal = min(matrix[n-1][i], minVal)
  return min(matrix[-1])

# in this main focus is to at any cell, what is min value of above values....whatever is min 
# then add with matrix[i][j]..at last row find min..