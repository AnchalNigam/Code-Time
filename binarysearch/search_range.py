class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def findLeftIndices(self, A, B):
        low = 0 
        high = len(A) - 1
        currIdx = -1
        while low <= high:
            mid = low + (high-low)//2
            if A[mid] == B:
                currIdx = mid
                high = mid-1
            elif A[mid] < B:
                low = mid + 1
            else: 
                high = mid - 1
        return currIdx
            
    def findRightIndices(self, A, B):
        low = 0 
        high = len(A) - 1
        currIdx = -1
        while low <= high:
            mid = low + (high-low)//2
            if A[mid] == B:
                currIdx = mid
                low = mid+1
            elif A[mid] < B:
                low = mid + 1
            else: 
                high = mid - 1
        return currIdx

            


    def searchRange(self, A, B):
        result = [-1, -1]
        result[0] = self.findLeftIndices(A, B)
        result[1] = self.findRightIndices(A, B)
        return result
       
# check nick white video for explanation but here only thing is ki we are trying to find 
# left half start indices and right half indices using two seaparate function