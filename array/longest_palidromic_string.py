# o(n2) and o(n2) space complexity 
# here basically firt hum ek 2d array maintain kr rhe hai jisme 1 length k lie 1 bhar rhe
# the 2 length ka dekh rhe then 2 se jyda ka dekh rhe hai so 2 se jyda me if border char ar 
# equal and dp[i+1] == d[[j-1]] then palindrome hai
maxStr = ""
string = ""
if len(s) == 0:
    return string
dp = [[0 for idx in range(len(s))] for idx2 in range(len(s))]

for idx in range(len(s)):
    dp[idx][idx] = 1
maxStr = s[0]
for idx in range(len(s)-1):
    string = s[idx]
    if s[idx] == s[idx+1]:
        string += s[idx+1]
        dp[idx][idx+1] = 1
        if len(maxStr) < len(string):
            maxStr = string
for k in range(2, len(s)):
    i = 0
    j = k+i
    while j < len(s):
        if s[i] == s[j] and dp[i+1][j-1]:
            string = s[i:j+1]
            dp[i][j] = 1
            if len(maxStr) < len(string):
                maxStr = string
        i += 1
        j = k+i
return maxStr

