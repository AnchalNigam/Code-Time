# def detectCycle(graph):
#   n = 9
#   visited = set()
#   dfsVisit = set()
#   def isCyclic(node):
#     stack = []
#     stack.append(node)
#     while stack:
#       # print(queue)
#       vertex = stack[len(stack)-1]
#       visited.add(vertex)
#       dfsVisit.add(vertex)
#       flag = False
#       # print(vertex)
#       for neighbour in graph[vertex]:
#         # print(neighbour, visited)
#         if neighbour not in visited:
#           flag = True
#           stack.append(neighbour)
#           # print(neighbour in visited, visited, neighbour)
#         elif neighbour in dfsVisit:
#           return True
#       if len(graph[vertex]) == 0 or not flag:
#         dfsVisit.remove(stack.pop())
#     return False
#   for v in range(1, n):
#     if v not in visited:
#       if(isCyclic(v)):
#         return True
#   return False
# graph = {
#   1: [2],
#   2: [3],
#   3: [4, 6],
#   4: [5],
#   5: [],
#   6: [5],
#   7: [8],
#   8: [9],
#   9: [7]
# } 
# print(detectCycle(graph))

def detectCycleDirected(graph):
  n = 9
  visited = set()
  dfsVisit = set()
  def isCyclic(node):
    visited.add(node)
    dfsVisit.add(node)
    print(dfsVisit, node)
    for neighbour in graph[node]:
      if neighbour not in visited:
        if(isCyclic(neighbour)):
          return True
      elif neighbour in dfsVisit:
        return True
    dfsVisit.remove(node)
    return False
  for v in range(1, n):
    if v not in visited:
      if(isCyclic(v)):
        return True
  return False
graph = {
  1: [2],
  2: [3],
  3: [4, 6],
  4: [5],
  5: [],
  6: [5],
  7: [2, 8],
  8: [9],
  9: [7]
} 
print(detectCycleDirected(graph))


# here main logic is agr koi node hmne process ki from path and we are going back then dfs visit se
# use hata do..because wo us path se process h gye hai...if agr path se ate hai and dfs visit me
# unvisited mark h then its not cycle where hai agr visited then there is cycle
# https://www.youtube.com/watch?v=uzVUw90ZFIg&t=1s
# course schdule 1 dekhna whn cycle detectn hua h bt without taking two sets ..one set se ...interes
# ingly hua h check

# undirected graph algo will not work see youtubechanel eg because isme directn dia h toh 
# directn k bhi dekhna padega 1 to 2 is not 2 to 1 