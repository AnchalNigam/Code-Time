# in this algo, main scene is use bfs technique but use priority queue why?
# because here edges are coming with weights and weights obvio j kam hga that we will
# take..and if we have visited any node with less weight then why to again wvisit that 
# node with higher wight. ao visited aray to track visited node and always less wight will be at top
# wil give prioerity to viist further node and again heapify will make smaller node at top
# my doubt came why prioerty because aagle jake shorter dis h skta hai but isme scene kya hta hai
# hare paas initially j node 1st node enter ki the queue me toh uska higher wight wala hga 
# but hm prioroty chota wale k de rhe hai and dete rhnge but if we find that further path 
# lesser then will switch to that path and for every node multiple path hga toh chote wale se h
# pahuchnge yahn


# time complexiy - (N+E)log N - (n is nde, e is edges, logn is becaue of priority queue)
# space is o(n)+o(n) - prioerity queue+dis



graph = { 
  # (1, 4)- 1 is distance and 4 is node
  1: [(2,2), (1,4)],
  2: [(5,5), (4, 3), (2,1)],
  3: [(4,2),(1,5),(3,4)],
  4: [(1,1),(3,3)],
  5: [(5,2),(1,3)]
}

def dijkstra(graph,s, n):
  dis = [float('inf')] * (n+1)
  unvisited_queue = [(0, s)]
  visited = set()
  dis[s] = 0
  import heapq
  heapq.heapify(unvisited_queue)
  while len(unvisited_queue) > 0:
    _, vertex = heapq.heappop(unvisited_queue)
    print(vertex)
    if vertex in visited:
      continue
    visited.add(vertex)
    for neighbour in graph[vertex]:
      w, v = neighbour
      if v not in visited: 
        # print(v, w, 'checking')
        newWeight = dis[vertex] + w
        if dis[v] > newWeight:
          dis[v] = newWeight
          heapq.heappush(unvisited_queue,(dis[v], v))    # see this dis[v] ye store krte h not w

  print(dis, 'check')

dijkstra(graph, 1, 5)


# time complexity - o(n+e)logn as n is nodes, e is jite edges hnge us node tak wo and logn for priorty queue
# space complexity - priority queue and dis, o(n+n)

# here we ae maintaining visited as weell beccause agr jaise 3 node h that will come at top
# pioity queue k wjh se(4,3) toh iska mtlb if we are visiting that node toh shortest path se h visit 
# krnge because of priority queue concept....now av 2 k through aye(6, 3) so its already visited 
# toh account me nhi lenge and shi bi hai because 6 toh bada h 4 se so dijksta me if you have added
# any vertex toh wo chote sbse upr hge and visited mark kr skte hai

# another thing- dont put distance at 1 index of tuple that will not work properly
# always put it at 0 index