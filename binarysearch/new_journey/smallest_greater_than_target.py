def nextGreatestLetter(letters, target):
    low = 0
    high = len(letters)-1
    while low <= high:
        mid = low + ((high-low)//2)
        if letters[mid] > target:
            high = mid-1
        else:
            low = mid+1
    return letters[low] if low < len(letters) else letters[0]
    
    
# basic thinking here is we will try to find out greater element and that we know
# if mid < target that means wo right side me hai and if greater then we should find out kahin isse 
# chota kuch toh nhi toh converge kro by high=mid-1 and findout smalles larger elem greater than target
# so ye thought se i solved it 
# time  - o(logn)