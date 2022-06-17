# def check(password):
#     n = len(password)
#     lc = 0
#     uc = 0
#     dc = 0
#     sc = 0
#     scDict = {
#         '!': 1,
#         '@': 1,
#         '#': 1,
#         '$': 1,
#         '%': 1,
#         '^': 1,
#         '&': 1,
#         '*': 1,
#         '(': 1,
#         ')': 1,
#         '-': 1,
#         '+': 1
#     }
#     if n < 8:
#         return False
#     for i in range(n):
#       print(password[i], 'check', password[i] in scDict)
#       if(i+1 < n and password[i] == password[i+1]):
#           return False
#       elif password[i] in scDict:
#         sc += 1
#       elif password[i].isupper():
#           uc += 1
#       elif password[i].islower():
#           lc += 1
#       elif password[i].isdigit():
#           dc += 1
       
#     print(sc, dc, uc, lc)
#     if sc >= 1 and dc >= 1 and uc >= 1 and lc >= 1:
#         return True
#     return False
            
# print(check("Me+You--IsMyDream"))
spells = [15,39,38,35,33,25,31,12,40,27,29,16,22,24,7,36,29,34,24,9,11,35,21,3,33,10,9,27,35,17,14,3,35,35,39,23,35,14,31,7]


potions = [25,19,30,37,14,30,38,22,38,38,26,33,34,23,40,28,15,29,36,39,39,37,32,38,8,17,39,20,4,39,39,7,30,35,29,23]
success = 317

import math
potionsLen = len(potions)
potions.sort()
print(potions, 'potions')
def nextGreatestLetter(target):
    low = 0
    high = len(potions)-1
    while low <= high:
        mid = low + ((high-low)//2)
        if potions[mid] == target:
          while(low >= 0 and potions[mid] == target):
            mid = mid - 1
          return mid+1
        elif potions[mid] > target:
          high = mid-1
        else:
          low = mid+1
    return low
result = []
# index = nextGreatestLetter(2)
# print(index)
for i in range(len(spells)):
    reqNum = math.ceil(success/spells[i])
    index = nextGreatestLetter(reqNum)
    print(index, reqNum)
    result.append(potionsLen-index)
print(result)


    
            
             