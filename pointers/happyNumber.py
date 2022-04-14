def happyNum(n):
  def solve(nums, dic):           
    if nums == 1:
        return True
    if nums < 1: 
        return False
    tempNums = str(nums)
    summation = 0
    
    for digit in tempNums:
        summation += (int(digit)**2)
    if summation not in dic:
        dic[summation] = 1
    else:
        return False            
    return solve(summation, dic)
  return solve(n, {})

n = 19
print(happyNum(n))

# i learned from this prob that focus on solving the prob rather than optimsed sol...think frst level
# make mistakes analyze the mistakes , improve algo and so on...with this i solved it in 99% faster yoo
# for adding numbers i used loop and str conversion 
# we could imporve it by using below approach, here we are diving number and adding -cool na...
# from today onwards asa sa approach le skte hai 
squareSum = 0
while (n > 0):
  remain = n%10
  squareSum += remain*remain
  n /= 10

          