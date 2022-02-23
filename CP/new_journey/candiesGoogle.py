def getRemainingCandy(candyArr, kids):
    totalCandies = 0
    for candies in candyArr:
        print
        totalCandies += candies
    return totalCandies%kids
    
numOfCases = int(input())
for caseNum in range(numOfCases):
    (bags, kids) = tuple(map(int, input().split()))
    candyArr = map(int, input().split())
    
    remainingCandy = getRemainingCandy(candyArr, kids)
    print(f"Case #{caseNum}: {remainingCandy}")