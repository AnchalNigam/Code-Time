# graph = {
#   3 : [5],
#   5 : [3,6,10],
#   6 : [5,7],
#   10 : [5,9],
#   9: [10,8],
#   7: [6,8],
#   8: [9,7],
#   11: [8]
#   }
# one way to represent graph is above way but noramally in questions thegive aray of array to 
# to represent edges and vertices
# graph =  {
#   1: [2],
#   2: [1,4]
# }


# from collections import defaultdict


# def detectCycle(edges):
#   graph = defaultdict(list)
#   # print(graph)
#   visited = set()
#   queue = []
#   for node1, node2 in edges:
#     graph[node1].append(node2)
#     # for undeirected graphs thats why on both nodes we are maintaing
#     graph[node2].append(node1) 
#   # print(graph)
#   queue.append((edges[0][0], -1))
#   visited.add(edges[0][0])
#   while len(queue) != 0:
#     vertex = queue.pop(0)
#     print(vertex, 'vertex b')
#     if vertex[0] in graph:
#       for i in graph[vertex[0]]:
#         print(visited, 'check', vertex, i)
#         if i in visited and i != -1 and i != vertex[1]:
#           return True 
#         # print('checking', i, visited)
#         if i not in visited:
#           queue.append((i, vertex[0]))
#           visited.add(i)
#   return False

# edges = [  [1, 2],[1, 3],[2, 3],[1, 4],[4, 5]
#      ]
# print(detectCycle(edges))
# not sure whether its right or not....logic applied will see later
# check strivers series

# updated code (check this)
graph = {
  1: [2],
  2: [1, 4],
  3: [5],
  4: [2],
  5: [3,6,10],
  10: [5,9],
  6: [5,7],
  9: [10,8],
  7: [6, 8],
  8: [7, 9, 11],
  11: [8]
}

def detectCycle(graph):
  n = 11
  visited = set()
  def isCyclic(node):
    queue = []
    queue.append((node, -1))
    while queue:
      # print(queue)
      vertex, parent = queue.pop(0)
      visited.add(vertex)
      for neighbour in graph[vertex]:
        # print(neighbour, visited)
        if neighbour not in visited:

          queue.append((neighbour, vertex))
          # print(neighbour in visited, visited, neighbour)
        elif parent != neighbour:
          print(parent, neighbour)
          return True
    return False
  for v in range(1, n):
    if v not in visited:
      if(isCyclic(v)):
        return True
  return False
  
print(detectCycle(graph))


# here main thught is check above example, here 8 is visited using 9 wala path.
# when we come to 7 node, we check adjacent nodes which is 8 and 6, we checked 6 is visited
# yes it is visited so we check parent == neighbour hga toh mns no cycle. now we check 
# is 8 visited but here 8 is viisted meaning 8 shyd parent hga but nhi h because wo
# kisi aur path se traverse hua h thats why so ye h main thought h