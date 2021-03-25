def search(A : list, l : int, h : int, key : int):
    # Complete this function
    pivot = -1
    p1 = A[0]
    low = 0
    high = len(A)-1
    while low <= high:
        mid = low + ((high-low)//2)
        if(mid+1) < len(A):
            if A[mid] < A[mid+1] and p1 < A[mid]:
                low = mid+1
                p1 = A[mid]
            elif A[mid] < A[mid+1] and p1 > A[mid]:
                high = mid-1
            elif A[mid] > A[mid+1]:
                pivot = mid
                break
            else:
                low = mid+1
        else:
            break
    # print(pivot, 'test')
    if (A[0] <= key <= A[pivot]) and pivot != -1 :
        low = 0
        high = pivot
    elif pivot == -1:
        low = 0
        high = len(A)-1
    else:
        low = pivot+1
        high = len(A)-1
    # print(low, high, 'checkig')
    def binarySearch(arr, l, h, k):
        low = l
        high = h
        while low <= high:
            mid = low + (high-low)//2
            if arr[mid] == k:
                return mid
            elif arr[mid] < k:
                low = mid+1
            else:
                high = mid-1
        return -1
    return binarySearch(A, low, high, key)
      