T = int(input())
finalChefDarthWinStatus = []
def chefDarthWar(chefDarthHealth):
  while chefDarthHealth[0] > 0 and chefDarthHealth[1] > 0:
    chefDarthHealth[0] = int(chefDarthHealth[0]-chefDarthHealth[1])
    chefDarthHealth[1] = int(chefDarthHealth[1]/2)
    # print(chefDarthHealth)
  if chefDarthHealth[0] <= chefDarthHealth[1]:
    return 1
  else:
    return 0

for t in range(T):
  chefDarthHealth = list(map(int,input().split()))
  finalChefDarthWinStatus.append(chefDarthWar(chefDarthHealth))

for warResult in finalChefDarthWinStatus:
  print(warResult)

