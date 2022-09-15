class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        minOps = float('inf')
        ops = 0
        start = 0
        end = 0
        n = len(blocks)
        x = 0
        while (end-start) < k and end < n:
            if blocks[end] == 'W':
                ops += 1
            if (end-start) == k-1:
                minOps = min(minOps, ops)
                if blocks[start] == 'W':
                    ops -= 1                   
                start += 1
            end += 1
            
        return minOps if minOps != float('inf') else 0

# lsiding window technique, using window and then dec inc acc and maintain min ops 
# time compelxity - o(n)