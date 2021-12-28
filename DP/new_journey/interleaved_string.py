def isInterleaving(X, Y, S, T):
 
    # return true if the end of all strings is reached
    if not X and not Y and not S:
        return True
 
    # return false if the end of string 'S' is reached,
    # but 'X' or 'Y' is not empty
    if not S:
        return False
 
    # calculate a unique key by using delimiter `|`
    key = (X, Y, S) 
    # if the subproblem is seen for the first time
    if key not in T:
 
        # if string 'X' is not empty and its first character matches with the
        # first character of 'S', recur for the remaining substring
        x = (len(X) and S[0] == X[0]) and isInterleaving(X[1:], Y, S[1:], T)
 
        # if string 'Y' is not empty and its first character matches with the
        # first character of 'S', recur for the remaining substring
        y = (len(Y) and S[0] == Y[0]) and isInterleaving(X, Y[1:], S[1:], T)
 
        T[key] = x or y
 
    return T[key]
 
 
if __name__ == '__main__':
 
    X = 'ab'
    Y = 'ab'
    S = 'abab'

    # dictionary to store solution to already computed subproblems
    T = {}
 
    if isInterleaving(X, Y, S, T):
        print('Interleaving')
    else:
        print('Not an Interleaving')
   



# def isSubsequence(s, t):
#   if len(s) == 0:
#     return True
#   matchingCount = len(s)
#   counter = 0
#   for i in range(len(t)):
#     if s[counter] == t[i]:
#         matchingCount -= 1
#         counter += 1
#     if matchingCount == 0:
#       break
#   return matchingCount == 0

 

# def get_all_substrings(string):
#   length = len(string)
#   alist = []
#   for i in range(length):
#     for j in range(i,length):
#       alist.append(string[i:j + 1]) 
#   return alist

# s1 = "YX"
# s2 = "X"
# s3 = "XXY"
