
from re import L


def isAlmostBalanced(freq,substr, L, R):
  # print(subStr, L, R)
  if ((R-L)+1)%2 == 0:
    return 0
  mid = L + (R-L)//2
  a = abs(freq[s[mid-1]]-freq[L-1])
  b = abs(freq[mid]-freq[R-1])
  return 1 if abs(a-b) == 1 else 0
def computeStringFreq(s):
  freq = [0]*26
  n = len(s)
  for i in range(n):
    freq[ord(s[i])-97] += 1
  for i in range(1, 26):
    freq[i] += freq[i-1]
  return freq

s = "singingbanana"
freq = computeStringFreq(s)
print(freq)
print(isAlmostBalanced(freq, s[7:12], 8, 12))


# s = "abac"


          
# file1=open("perfectly_balanced_chapter_1_validation_input.txt","r")
# file2=open("perfectly_balanced_chapter_1_op.txt","w")

# # Iterate over each line in the file
# lineC = 0
# caseC = 0
# lines = file1.readlines()
# # lines = [i for i in lines if i]
# line = 1
# while line < len(lines):
#   lines[line] = lines[line].strip('\n')
#   s = lines[line]
#   line += 1
#   ans = 0
#   N = int(lines[line])
#   for row in range(N):
#     line += 1
#     L, R = map(int, lines[line].split())
#     # print(s[L-1: R])
#     if(isAlmostBalanced(s[L-1: R], L, R)):
#       ans += 1
#   lineC += 1
#   file2.write("{}{}{} {}".format("Case #", lineC, ":", str(ans)))
#   file2.write("\n")
#   line += 1

    
# # Release used resources
# file1.close()
# file2.close()
