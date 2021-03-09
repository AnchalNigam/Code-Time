def maxProfit():
  prices = [1,2,3,4,5]
  maxProfit = 0
  buy = 0
  for idx in range(len(prices)-1):
    if prices[idx] < prices[idx+1] and buy == 0:
      cp = prices[idx]
      print(prices[idx])
      buy = 1
    elif prices[idx] > prices[idx+1] and buy == 1:
      maxProfit += prices[idx]-cp
      buy = 0
  if buy == 1:
    maxProfit += prices[idx+1]-cp
  return maxProfit

print(maxProfit())