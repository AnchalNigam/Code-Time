class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
      trackArr = []
      row = 9
      for i in range(row):
          for j in range(row):
              if board[i][j] in trackArr:
                  print(trackArr, board[i][j])
                  return False
              elif board[i][j] != '.':
                  trackArr.append(board[i][j])
          trackArr = []
      print('test')
      trackArr = []
      for i in range(row):
          for j in range(row):
              if board[j][i] in trackArr:
                  return False
              elif board[j][i] != '.':
                  trackArr.append(board[j][i])
          trackArr = []
      gridR = 0
      gridC = 0
      trackArr = []
      while gridR < 3 and gridC < 3:
          for i in range(gridR*3, gridR*3+3):
              for j in range(gridC*3, gridC*3+3):
                  if board[i][j] in trackArr:
                      return False
                  elif board[i][j] != '.':
                      trackArr.append(board[i][j])
          trackArr = []
          if gridC == 2:
              gridR += 1
              gridC = 0
          else:
              gridC += 1
      return True
# time complexity o(k) k is row* column = n*2
# space complexity o(k) k is row*column
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dic = {}
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    str1 = "row" + str(i) + str(board[i][j])
                    str2 = "col" + str(j) + str(board[i][j])
                    str3 = "box" + str(i//3) + str(j//3) + str(board[i][j])
                    print(str1, str2, str3)
                    if str1 not in dic and str2 not in dic and str3 not in dic:
                        dic[str1] = True
                        dic[str2] = True
                        dic[str3] = True
                    else:
                        return False
        return True

