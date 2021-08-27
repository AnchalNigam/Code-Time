
def rotate(A):
    n = len(A)
    for i in range(n):
        for j in range(i, n):
            temp = A[i][j]
            A[i][j] = A[j][i]
            A[j][i] = temp
    
    for i in range (n):
        for j in range(n//2):
            temp = A[i][j]
            A[i][j] = A[i][n-1-j]
            A[i][n-1-j] = temp

    return A
print(rotate([[1,2],[3,4]]))
