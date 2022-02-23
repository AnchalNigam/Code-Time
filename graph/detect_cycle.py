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


from collections import defaultdict


def detectCycle(edges):
  graph = defaultdict(list)
  # print(graph)
  visited = set()
  queue = []
  for node1, node2 in edges:
    graph[node1].append(node2)
    # for undeirected graphs thats why on both nodes we are maintaing
    graph[node2].append(node1) 
  # print(graph)
  queue.append((edges[0][0], -1))
  visited.add(edges[0][0])
  while len(queue) != 0:
    vertex = queue.pop(0)
    print(vertex, 'vertex b')
    if vertex[0] in graph:
      for i in graph[vertex[0]]:
        print(visited, 'check', vertex, i)
        if i in visited and i != -1 and i != vertex[1]:
          return True 
        # print('checking', i, visited)
        if i not in visited:
          queue.append((i, vertex[0]))
          visited.add(i)
  return False

edges = [  [1, 2],[1, 3],[2, 3],[1, 4],[4, 5]
     ]
print(detectCycle(edges))
# not sure whether its right or not....logic applied will see later
# check strivers series