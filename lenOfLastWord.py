A = input()
def lengthOfLastWord(A):
  lenCount = 0
  lastStringLen = 0
  if len(A) == 0:
      return 0
  for idx in range(len(A)-1):
      if A[idx] == " " and A[idx+1] != " ":
          lastStringLen = lenCount
          lenCount = 0
      elif A[idx] != " ":
          lenCount += 1
  if A[len(A)-1] != " ":
      lastStringLen = lenCount+1
  else:
      lastStringLen = lenCount
  return lastStringLen

lengthOfLastWord(A)