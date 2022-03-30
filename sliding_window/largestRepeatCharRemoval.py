def largestRepeatCharRemoval(s,k):
    dic = {}
    l = 0 
    r = 0
    maxVal = 0
    maxFreqCount = 0
    while r < len(s):
        if s[r] not in dic:
            dic[s[r]] = 1
        else:
            dic[s[r]] += 1
        maxFreqCount = max(maxFreqCount, dic[s[r]])
        while((r-l+1) - maxFreqCount > k):
            dic[s[l]] -= 1
            l += 1
        r += 1
        maxVal = max(maxVal, r-l)
    return maxVal

# unfortunately, could not solve.
# main strategy was that you have to maintain max occured char. obvio ek majrity toh hga hi
# jo major bana and j window size hai if you minus both it means wo diff character hai
# wo diff character ab k opratns se jyda hga mns invalid window...so now make valid window
# main confusing part ye h tha ki how we can again maintain maxfreqcount so here 
# we dont care who is max , we just reducing the window size till window valid na h jate
# as max freq count wale window ka ans toh capture ho gya h aage k window valid krne h 
# so just dec it ..aisa sa logic laga
# complexity whi o(N)