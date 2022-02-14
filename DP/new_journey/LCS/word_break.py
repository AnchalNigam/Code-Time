# def longestCommonString(text1, text2):
#   n1 = len(text1)
#   n2 = len(text2)
#   dp = [[0 for i in range(n2+1)] for j in range(n1+1)]
#   maxx = 0
#   minnx = 1


#   for i in range(1, n1+1):
#     for j in range(1, n2+1):
#       if text1[i-1] == text2[j-1]:
#         dp[i][j] = 1 + dp[i-1][j-1]
#         if(maxx<dp[i][j]):
#           maxx=dp[i][j]
                
#       else:
#         dp[i][j] = 0
#   for i in range(1, n1+1):
#     for j in range(1, n2+1):
#       if(dp[i][j] == 1 and (i  < n1 and j < n2 and  dp[i+1][j+1] > 1)):
#         minnx = j
#         break
#   # print(dp)
#   new_string = ""
#   for i in range(len(text2)):
#     if not (i >= minnx - 1 and i < (maxx+minnx)-1):
#       new_string += text2[i]
#   print(new_string, text1)
#   return new_string if minnx != 1 else text2


# def word(word_dict, t):
#   new_string = t
#   # longestCommonString("dog", t)
#   for word in word_dict:
#     new_string = longestCommonString(word, new_string)
#     print(new_string)
#   if new_string == "" or (new_string in word_dict):
#     return True
#   return False
#   # print(new_string)




# word_dict = ["a","abc","b","cd"]
# t = "abcd"

# print(word(word_dict, t))




def wordBreak(t, word_dict):
  final = [False]
  def solve(new, ans):
    if len(new) == 0:
      final[0] = True
      return
    for i in range(len(new)):
      # print(new[:i+1])
      left = new[:i+1]
      if left in word_dict:
        solve(new[i+1:], left)
    return
  solve(t, "")
  return final[0]


# word_dict = ["a","abc","b","cd"]
# t = "abcd"
word_dict = ["apple","pen"]
t = "applepenapple"
print(wordBreak(t, word_dict))




