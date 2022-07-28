from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        prefix = mat[:][:]
        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j!=0:
                    prefix[i][j] += prefix[i][j-1]
                elif j == 0 and i != 0:
                    prefix[i][j] += prefix[i-1][j]
                elif i != 0 or j != 0:
                    prefix[i][j] += (prefix[i-1][j]+prefix[i][j-1]-prefix[i-1][j-1])
        # print(prefix, 'check')
                    
                    
      
        result = []
        for i in range(m):
            rl = max(i-k, 0)
            ru = min(i+k, m-1)
            temp = []
            for j in range(n):
                cl = max(j-k, 0)
                cu = min(j+k, n-1)
                # print(rl, cu, cl, ru, 'll')
                value = prefix[ru][cu]
                if rl-1 >=0  and cl-1 >= 0:
                    # print('inside')
                    value += prefix[rl-1][cl-1]
                if rl-1 >= 0 :
                    # print('inside2')
                    value -= prefix[rl-1][cu]
                if cl-1 >= 0:
                    # print('inside3')
                    value -= prefix[ru][cl-1]
                temp.append(value)
            result.append(temp)
        return result
                
        
# https://computersciencesource.wordpress.com/2010/09/03/computer-vision-the-integral-image/
# check this..here prefix sum ka logic laga h we have maintain sum of all over matirx
# then wo precomputed value k - kr rhe h ...upar wale blogs k dekhna ..usme ek particular
# block kaisa sum nikal rhe h hai..main prefix sum banane me diagonals left k add kia h 
# and right diagnonal me upper elem k - because wo left diagnols me uska sum hai h
# toh us right dignol k upper cell k value thde lenge so in this way matrix bante h 
# usme ek particular block kaisa sum nikal rhe h hai wo blog me hai
# 