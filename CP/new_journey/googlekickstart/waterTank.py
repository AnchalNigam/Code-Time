T = int(input())
import math
def waterTank(N, Q, queries):
  tree = [[[1, 0]]]
  for i in range(1, N-1):
    x1 = 2**i
    x2 = 2**(i+1)-1
    tree.append([x, 0] for x in range(x1, x2+1))
  c = 0
  # print(tree)
  for k in range(Q):
    t = int(math.log(queries[k],2))
    for i in range(c, t+1):
      n1 = len(tree[i])
      for j in range(n1):
        # print(tree[i][j], 'll')
        if tree[i][j][1] != 1:
            tree[i][j][1] += 1/n1
            if tree[i][j][1] == 1:
              c += 1
  return c



for t in range(T):
  N, Q = list(map(int, input().split()))
  for i in range(N-1):
    input()
    
  queries = []
  for i in range(Q):
    queries.append(int(input()))
  # print(queries, 'check')
  print(f"Case #{t+1}: {waterTank(N, Q, queries)}")