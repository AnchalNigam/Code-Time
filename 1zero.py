def maxLen(n, lis):
    #code here
    oneIndexes = []
    zeroes = 0
    minIndex = 0
    for idx,value in enumerate(lis):
        if value == 1:
            oneIndexes.append(idx)
    if len(oneIndexes) != 0:
        for idx in range(oneIndexes[0]):
            if value == 0:
                zeroes += 1
        for i in range(1,len(oneIndexes)):
            zeroes += oneIndexes[i]-oneIndexes[i-1]-1
        minIndex = oneIndexes[0]
        maxIndex = oneIndexes[len(oneIndexes)-1]
        if oneIndexes[0] - (abs(zeroes-len(oneIndexes))) >= 0:
            minIndex = oneIndexes[0] - (abs(zeroes-len(oneIndexes)))
        else:
            maxIndex = oneIndexes[len(oneIndexes)-1] + (abs(zeroes-len(oneIndexes)))
    else:
        return 0
    return (maxIndex-minIndex)+1
    
        