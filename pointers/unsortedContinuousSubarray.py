def unsortedContinuousSubArray(nums):
    n = len(nums)
    if n <= 1:
        return 0
    p1 = 0
    p2 = n-1
    
    while p1 < len(nums) - 1 and nums[p1] <= nums[p1 + 1]:
        p1 += 1
    
    while p2 > 0 and nums[p2] >= nums[p2 -1]:
        p2 -= 1
        
    if p1 > p2:
        return 0
    # print(p1, p2)
    mini = float('inf')
    maxi = float('-inf')
    
    for i in range(p1,p2+1):
        mini = min(mini, nums[i])
        maxi = max(maxi, nums[i])
    # print(maxi, mini, 'check')
    while p1 > 0 and nums[p1-1] > mini:            
        p1 -= 1
    while p2 < n-1 and nums[p2+1] < maxi:
        p2 += 1
    # print(p1, p2)
    return 0 if p2-p1+1 < 0 else p2-p1+1

nums = [1,2,3,4,5]
print(unsortedContinuousSubArray(nums))
        

# here two soltn can be  proposed -
# 1. sort the array and match element by element, whereevr is the diff store min and max acc.
# second one is above....here we are finding the point where pattern gets distorted like i+1 < i
# after finding that point, we find min in between those points and then backward traverse
# krke ye findout krte kya koi usse < hai if yes then decrementing the counter else wo whi rhega
# in this way we find that point