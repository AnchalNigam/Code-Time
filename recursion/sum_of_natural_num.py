def sumOfNaturalNum(n):
  if(n == 1):
    return 1
  return sumOfNaturalNum(n-1) + n
print(sumOfNaturalNum(10))