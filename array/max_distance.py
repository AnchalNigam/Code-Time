class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        if len(A) <= 1:
            return 0
        indexTrace = []
        for idx in range(len(A)):
            indexTrace.append((A[idx], idx))
        indexTrace.sort(key=lambda x: x[0])
        minInx = float("inf")
        result = 0
        for idx in range(len(indexTrace)):
            minInx = min(minInx, indexTrace[idx][1])
            result = max(result, indexTrace[idx][1] - minInx)
        return result


# in this, firstly lets sort the array with mainting index. this will fulfil the A[i]<=A[j] constraint
# then now lets find out max j-i, firstly find min of i and also the case can be ki min i at last me ho
# but that means that would not be max j-i, as wo element start me tha original array me
# so it means min i not neessary gives max of j - ithats why we have manintained other var
# thats tracking the max of j - min(i) if min(i)-j is max than already stored res then store it else skip
