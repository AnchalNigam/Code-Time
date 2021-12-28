def matrixReshape(mat, r, c):
    noOfElem = 0
    for i in range(len(mat)):
        col = len(mat[i])
        noOfElem += col
    if noOfElem > r*c or noOfElem < r*c:
        return mat
    res = []
    rowC = 0
    colC = 0
    for i in range(r):
        subArr = []
        for j in range(c):
            subArr.append(mat[rowC][colC])
            colC += 1
            if colC == col:
                rowC += 1
                colC = 0
        res.append(subArr)
    return res
              
              
          
      