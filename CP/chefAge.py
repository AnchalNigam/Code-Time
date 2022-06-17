T = int(input())
result = []
def equalDistribution(inputs):
  totalChoco = inputs[0] + inputs[1]
  return 'YES' if totalChoco % 2 == 0 else 'NO'

for t in range(T):
  inputs = list(map(int,input().split()))
  result.append(equalDistribution(inputs))

for res in result:
  print(res)
