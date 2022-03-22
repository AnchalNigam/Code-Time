

def allPathTraverse(grid):
  result = []
  def solve(i, j, res):
    print(i, j, res, '===================>')
    if i == len(grid)-1 and j == len(grid[0])-1:
      print('inside')
      result.append(res+grid[i][j])
      return 
    if i >= len(grid) or j >= len(grid[0]):
      return
   
     
    res += grid[i][j]
    # curC = grid[i][j]
    # grid[i][j] = "*"
    # print(res, 'resss')
    solve(i, j+1, res)
    solve(i+1, j, res)
    # res = res[:-1]
    
  solve(0,0, "")
  return result
    
# def allPathTraverse(grid):
#   result = []
#   def solve(i, j, res):
#     if i == len(grid)-1 and j == len(grid[0])-1:
#       result.append(res+[grid[i][j]])
#       return 
#     if i >= len(grid) or j >= len(grid[0]):
#       return
   
     
#     res.append(grid[i][j])
#     # curC = grid[i][j]
#     # grid[i][j] = "*"
#     # print(res, 'resss')
#     solve(i, j+1, res)
#     solve(i+1, j, res)
#     res.pop()
#     # res = res[:-1]
    
#   solve(0,0, [])
#   return result

# grid = [['A']]

grid = [['A', 'B', 'C'], ['D', 'E','F'], ['G', 'H', 'I']]
# grid = [[1,2,3], [4,5,6], [7,8,9]]

print(allPathTraverse(grid))

# here when we are taking array then as we know in recursive calls, maintain rhta h sttate so it 
# need to update for previous call thats why pop whereas is string aall np need as in re
# recursive calls no alreatn of variable takes place,,,,,woww