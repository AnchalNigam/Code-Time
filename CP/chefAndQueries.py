T = int(input())
chefAndQueriesStatus = []
# 12 3 4 2
def chefAndQueries(k, chefAndQueriesArr):
  return (sum(chefAndQueriesArr)//k)+1





for t in range(T):
  chefQueryData = list(map(int,input().split()))
  chefAndQueriesArr = list(map(int,input().split()))
  chefAndQueriesStatus.append(chefAndQueries(chefQueryData[1], chefAndQueriesArr))

for result in chefAndQueriesStatus:
  print(result)

