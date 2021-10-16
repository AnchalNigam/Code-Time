class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low = 0 
        high = len(letters)-1
        n = len(letters)
        res = 0
        while low <= high:
            mid = low + (high-low)//2
            if letters[mid] == target:
                res = mid+1
                low = mid + 1
            elif letters[mid] > target:
                res = mid
                print(letters[mid])
                high = mid-1
            else:
                low = mid+1
        print(res)
        return letters[res%n]
            
                
                
# we are applying bs and storing result at res and modules of n as target can be last elem
# so we need to return first elem in that case(basically circular search)