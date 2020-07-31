T = input()
#100 180 260 310 40 535 695
def maxProfit(arr):
  maxProfit = 0
  minPrice = arr[0]
  lastSellDay = -1
  currentSellDay = -1
  sellBuyData  = []
  for idx,value in enumerate(arr):
    
    if (maxProfit < (value - minPrice)):
      maxProfit = value - minPrice
    elif (maxProfit > (value - minPrice)):
      lastSellDay = currentSellDay + 1
      currentSellDay = idx - 1
      if (currentSellDay != lastSellDay):
        day = "(" + str(lastSellDay) + ' ' + str(currentSellDay) + ")" 
        sellBuyData.append(day)
        maxProfit = 0
        minPrice = value
      else:
        lastSellDay += 1
    if value < minPrice:
      minPrice = value
      lastSellDay = idx
  lastSellDay = currentSellDay + 1
  currentSellDay = idx
  if (currentSellDay != lastSellDay):
    sellBuyData.append( "(" + str(lastSellDay) + ' ' + str(currentSellDay) + ")" )
  if len(sellBuyData) == 0:
    return 'No Profit'
  else:

    return ' '.join(map(str,sellBuyData)) 
  


for i in range(int(T)):
  numDays = int(input())
  arr = input().split()
  arr = list(map(int, arr))
  print(maxProfit(arr))
