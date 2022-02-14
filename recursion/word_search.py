

def wordSearch(board, word):
  m = len(board)
  n = len(board[0])
  result = [False]

  def solve(i, j, res, counter):
    # print(counter, len(word))
    if counter == len(word):
      return True
    if i < 0 or j < 0 or i >= m or j >= n:
      return False
    if(board[i][j] != word[counter]):
      return False
 
    print(counter, board[i][j])
    if word[counter] == board[i][j]:
      curC = board[i][j]
      board[i][j] = '*'
      counter += 1
      if(not res):
        res = solve(i-1, j, res, counter)
      if(not res):
        print('inside', i, j, counter, res)
        res = solve(i, j+1, res, counter)
      if(not res):
        res = solve(i+1, j, res, counter)
    
      if(not res):
        res = solve(i, j-1, res, counter)
      print('outside', i, j, counter, res)
      counter -= 1
      board[i][j] = curC
    return res

  for row in range(m):
    for col in range(n):
      if(solve(row, col, False, 0)):
        return True
  return result[0]

board =[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
print(wordSearch(board, "ABCB"))

# so happy, i did it...in this main funda is to loop through whole matrix and 
# for each element, checking all four directions, and maintaining counter 
# how many words has matched, if matching then we go and on to check other
# words until counter becomes equal to len(word) - this is base case
# we have also put if that board is visited then mark it as *, in one calc of that
# particular cell we do that. if suppose words not found at couter 2 or 3 then we have
# to again maintain the counter thats why -1 and also visted marked unmarked. main
# is visited ko kaise unmark kia