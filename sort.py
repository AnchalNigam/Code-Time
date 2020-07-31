# T = input()
# def sortArr(inputStr):
#   inputStr.sort()
#   print(*inputStr)
#   return 1


# for i in range(int(T)):
#   sizeArr = input()
#   arr = input().split()
#   print(sortArr(arr))

T = input()
def sortArr(inputStr):
  num1 = num2 = num0 = 0
  for i in inputStr:
    if i == '0':
      num0 += 1
    elif i == '1':
      num1 += 1
    else:
      num2 += 1
  return ' '.join(['0']*num0 + ['1']*num1 + ['2']*num2)

for i in range(int(T)):
  sizeArr = input()
  arr = input().split()
  print(sortArr(arr))