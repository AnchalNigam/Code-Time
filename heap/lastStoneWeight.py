def lastStoneWeight(stones):
    import heapq
    stones.sort()
    # print(stones)
    while len(stones) > 1 :
        n = len(stones) - 1
        x = stones[n]-stones[n-1]
        stones = stones[:n-1]
      
        if x != 0:
            stones.append(x)
        # print(stones)
        stones.sort()
    # print(stones)
    return stones[0] if len(stones) > 0 else 0
    