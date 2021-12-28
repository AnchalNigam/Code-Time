def isValidSudoku(board):
    for i in range(9):
      dic = {}
      for j in range(9):
        if  board[i][j] != '.' and board[i][j] not in dic:
          dic[board[i][j]] = 1
        elif board[i][j] != '.':
          return False
    for i in range(9):
      dic = {}
      for j in range(9):
          if  board[j][i] != '.' and board[j][i] not in dic:
              dic[board[j][i]] = 1
          elif board[j][i] != '.':
              return False
    
    dic = {}
    i = 0
    j = 0
    row = 0
    col = 0
    while i < 9 and i < row + 3:   
        while j < col + 3:
            if  board[i][j] != '.' and board[i][j] not in dic:
                dic[board[i][j]] = 1
            elif board[i][j] != '.':
                return False
            j += 1
        i += 1
        if i != row+3:
            j = col
        if i == row + 3 and j <= 6:   
            col += 3
            j = col
            i = row 
            dic = {}
        elif i < 9 and j == 9:                 
            row += 3
            i = row
            j = 0
            col = 0
            dic = {}
    return True