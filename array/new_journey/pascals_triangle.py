def pascalsGenerate(numRows):
    res = [[1]]
    if numRows == 1:
      return res
    for i in range(1, numRows):
      subRes = [1]
      for j in range(1, i):
        subRes.append(res[i-1][j-1]+res[i-1][j])
      subRes.append(1)
      res.append(subRes)
    return res
    