def decimalToBinary(num):
  if(num == 1):
    return '1'
  return decimalToBinary(num//2) + str(num%2)
  
print(decimalToBinary(33))