def maxProfit(prices):
  minimum = float('inf')
  profit = 0
  for idx in range(len(prices)):
    minimum = min(minimum, prices[idx])
    if((prices[idx]-minimum) > profit):
      profit = prices[idx]-minimum
  return profit

prices = [7,6,4,3,1]
print(maxProfit(prices))


# not related to dp.normal as well, i solved it