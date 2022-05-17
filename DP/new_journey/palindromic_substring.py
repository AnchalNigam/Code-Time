class Solution:
  def longestPalindrome(self, s: str) -> str:
      dp = [[0] * len(s) for i in range(len(s))]
      ans = ""
      max_length = 0
      for i in range(len(s) - 1, -1, -1):
          for j in range(i, len(s)):
              if s[i] == s[j] and (j - i < 3 or dp[i+1][j-1] == 1):
                  dp[i][j] = 1
                  if ans == "" or max_length < j - i + 1:
                      ans = s[i:j+1]
                      max_length = j - i + 1
      return ans

# finally i understood this questn what is the logic behind....
# frst way is brute force..u have taken one outer loop then inner loop from i+1 to n so 
# ye substrings banayega and from that substrings inside ek look lagega that will be check whether
# it is palindrome or not...so o(n3) hua...
# now think in dp, 
# 
# we have to use the previous computed value,
# frst define dp[i][j] here i is start of substr and j is end of substr....suppose i is 1 
# j is 3 matlb substr 1 to 3 k bat h rhe hai
#
# hwre scene is suppose there is abab string....start with a ..all diagonal save 1 as every
# single char is palindrome then ....b comes in check whether a and b equal if equal mns
# palindrome ...now a comes...check only start and last elem that is coming which is ca and start is
# a so it is  equal, now check for i+1 and j-1, check for substring (dp[i+1][j-1] - aba-> i+1= 1 and
# j-1 = 1 which is b that is palin so whole substring from 0 to 2 [a to c] is palicdrome
# now comes to b again check a to b again not equal...here hme dp table backward bharne hge
# last se shuru kro....3 to 3, yes palin...2 to 2 then 2 to 3 then 1 pe aao 1 to 1 then 1 to 2
# then 1 to 3 1 to 3 me hme edge wale chars dekhte h and then inside k next row se fetch krte h
# ki wo substr kya palin the k nhi and whole ans usse aa jata hai
# so o(n2) complexity hai... in this way memo hua...internal substring se whole sbstring ka answer
# compute kia....and backward bhara...ye interestng note krne wale chez h how memo is done
# for better understaning check this
# https://www.youtube.com/watch?v=WpYHNHofwjc