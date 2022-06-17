from collections import defaultdict

def alienDict(dic):
  graph = defaultdict(list)
  for i in range(len(dic)-1):
    for j in range(len(dic[i])):
      if dic[i][j] != dic[i+1][j]:
        graph[dic[i][j]].append(dic[i+1][j])
        break
  print(graph)
  stack = []
  stack.append(dic[0][0])
  visited = set()
  visited.add(dic[0][0])
  result = []
  while stack:
    vertex = stack[-1]
    if graph[vertex]:
      neighbour = graph[vertex].pop()
      if neighbour not in visited:
        stack.append(neighbour)
        visited.add(neighbour)

    else:
      poppedElem = stack.pop()
      result.append(poppedElem)

  print(result[::-1])

alienDict(["ywx", "wz", "xww", "xz", "zyy", "zwz"])


# i did it by own...microsoft questn is this....yoo man...o(v+e)- space - n, n

# so here main logic i used was its lexo sorted and from questn i got to know that dependent work 
# ques pattern hai isme..so topo use kr skte h bt for that we need to find the dependency of chars
# frst toh lexo ka logic lagaya -lexo sort mns whereveer char diff krta hai that matters..children
# chill me children will come frst because chil same h agla letter pe differ hua hai and d, l se pehle
# ata h so children < chill ..same logic i used in creatng graph ,whereever i got frst char diff 
# uska dependency bana di...ar graph prepare kr dia fr maine topo ka logic laga dia simple
