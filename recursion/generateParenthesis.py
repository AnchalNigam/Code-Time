from curses.ascii import NL
import re


def generateParanthesis(n):
  result = []
  def solve(open, close, res):
    if len(res) == n*2:
      result.append(res)
      return
    if open < n:
      solve(open+1, close, res+'(')
    if close < open:
      solve(open, close+1, res+')')


  solve(0, 0, "")
  return result

print(generateParanthesis(3))

# although i was not able to solve it....main funda i understood is take open brackt till n
# and then think of close bracker and consider them