def stockmax(prices):
  c=prices[len(prices)-1]
  a=0
  for i in range(len(prices)-1,-1,-1):
      if c<prices[i]:
          c=prices[i]
      a+=(c-prices[i])
  return a
