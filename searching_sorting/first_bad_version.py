class Solution:
  def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    low = 0
    high = n - 1
    badVersion = 0
    while low <= high:
        mid = low + (high - low) // 2
        if(isBadVersion(mid+1) and not isBadVersion(mid)):
            return mid+1
        elif(isBadVersion(mid+1)):
            high = mid - 1
        else:
            low = mid + 1
    return badVersion