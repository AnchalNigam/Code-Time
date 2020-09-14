A = "abbcccbbbcaaccbababcbcabca"
subStr = ""
# stack = []
# for char in A:
#   word += char
#   stack.append(char)
#   if word == word[::-1] and len(subStr) < len(word):
#     subStr = word
# for idx in range(len(stack)):
#   stack.pop(0)
#   print(stack)
#   if stack == stack[::-1] and len(subStr) < len(stack):
#     subStr = ''.join(stack)

# print(subStr)

# other way 0(n2)
word = "" 
for idx in range(len(A)):
  word = ""
  word += A[idx]
  for idx2 in range(idx+1, len(A)):
    word += A[idx2] 
    if word == word[::-1] and len(subStr) < len(word):
      subStr = word
if subStr == "":
  print(A[0])
print(subStr)