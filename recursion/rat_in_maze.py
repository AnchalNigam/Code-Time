def ratInMaze(m, n):
  result = []
  check = [False]
  def solve(i,j,res):
    # print(i,j, res)
    if i < 0 or j < 0 or i >=n or j >= n:
      return False
    if m[i][j] == 0:
      return False
    if m[i][j] == '*':
      return False
    if i == n-1 and j == n-1:
      print(res, 'res')
      if res == 'RRRRDLLLLDRRRRDLLLLDRRRR':
        check[0] = True
      # print('insidee')
      result.append(res[:])
      return
   
      # print(i, j, res, 'check')
    if m[i][j] == 1:
      curC = m[i][j]
      m[i][j] = '*'
      res += 'R'
      solve(i, j+1, res )
      res += 'D'
      solve(i+1, j, res)
      res += 'L'
      solve(i-1, j, res)
      res += 'U'
      solve(i, j-1, res)
      res = res[:-1]
      m[i][j] = curC
  solve(0,0,"")
  print(check)
  return check

n=5
m=[[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1],[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
print(ratInMaze(m,n))