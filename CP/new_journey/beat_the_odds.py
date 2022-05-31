# def beatTheOdds(nums):
#   i = 0
#   c = 0
#   while i < len(nums)-1:
#     if not ((nums[i]%2 == 0 and nums[i+1]%2 == 0) or (nums[i]%2 != 0 and nums[i+1]%2 != 0)):
#       c += 1
#       i += 1
#     i += 1
#   return c
      

# numOfCases = int(input())
# for cases in range(numOfCases):
#   n = input()
#   nums = list(map(int, input().split(' ')))
#   print(beatTheOdds(nums))

def miniMoneyNeed(giftsCount, giftPrize):
  giftPrize.sort()
  money = 0
  for i in range(giftsCount):
    money += giftPrize[i]
  return money

numOfCases = int(input())
for cases in range(numOfCases):
  giftsCount = int(input())
  n = input()
  gifts = list(map(int, input().split(' ')))
  print(miniMoneyNeed(giftsCount, gifts))