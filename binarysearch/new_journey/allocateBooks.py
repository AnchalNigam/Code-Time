

def allocateBooks(arr, n, m):

    # Write your code here
    # Return the minimum number of pages
    def feasibleDistribution(maxPages):
        total = 0
        student = 1
        for i in range(n):
            total += arr[i]
            if arr[i] > maxPages:
              return False
            if total > maxPages:
                student += 1
                total = arr[i]
        if student > m :
            return False
        return True
               
        
    low = min(arr)
    high = sum(arr)
    print(low, high)
    res = -1
    while low <= high:
        mid = low + (high-low)//2
        print(mid, low, high)
        if feasibleDistribution(mid):
            high = mid-1
            res = mid
        else:
            low = mid+1
    return res


arr = [5, 17, 100, 11]     
n = 4
m = 4
print(allocateBooks(arr, n, m))
