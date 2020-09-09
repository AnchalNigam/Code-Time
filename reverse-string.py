A = "       fwbpudnbrozzifml osdt ulc jsx kxorifrhubk ouhsuhf sswz qfho dqmy sn myq igjgip iwfcqq                 "
# one way wuthout any builtin function
def solve(A):
  word = ""
  reverseStr = ""
  for idx in range(len(A)-1, -1, -1):
      if A[idx] != " ":
        word = A[idx] + word
      else:
          if word != "":
              reverseStr += word + " "
              word = ""
  if word != "":
      reverseStr += word
  strippedReverseStr = ""
  if reverseStr[len(reverseStr)-1] == " ":
      for idx in range(len(reverseStr)-1):
          strippedReverseStr += reverseStr[idx]
  else:
      strippedReverseStr = reverseStr
  return strippedReverseStr

print(solve(A))


# other way using builtin  

# def solve(self, A):
#   arr = []
#   word = ""
#   for idx in range(len(A)):
#       if A[idx] != " ":
#         word += A[idx]
#       else:
#         if word != "":
#           arr.append(word)
#           word = ""
#   if word != "":
#       arr.append(word)
      
#   return ' '.join(arr[::-1])