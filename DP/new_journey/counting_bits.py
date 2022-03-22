def countingBits(n):
  result = [0]
  def findDecimal(n, count):
    if n == 1:
      count += 1
      return count
    if n%2 == 1:
      count += 1
    return findDecimal(n//2, count) 

  for i in range(1, n+1):
    decimal = findDecimal(i, 0)
    # print(decimal, i, 'kkkk')
    result.append(decimal)
  return result

print(countingBits(5))


# every time we keep dividing number(N) with 2 until we reach >=0 i.e 1.
# So we keep going like this N/2^0 , N/2^1 , N/2^2 , N/2^K . So that means in the end N/2^K = 1
# N=2^K
# logN = Klog2
# K=logN to base 2 so overall = logN.