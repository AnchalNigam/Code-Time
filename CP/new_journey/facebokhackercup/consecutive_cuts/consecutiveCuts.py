

def isItPossible(N, K, A, B):
  if K == 0:
    for i in range(N):
      if A[i] != B[i]:
        return 'NO'
    return 'YES'
  flag = False
  dic = {}
  for i in range(N):
    if A[i] != B[i]:
      flag = True
    if A[i] not in dic:
      dic[A[i]] = 1
    else:
      dic[A[i]] += 1
  if not flag:
    if N != 2:
      if K == 1 and len(dic.keys()) > 1:
        return 'NO'
      return 'YES'
  if N == 2:
    if len(dic.keys()) > 1:
      if not flag:
        if K%2 != 0:
          return 'NO'
        return 'YES'
      else:
        if K%2 == 0:
          return 'NO'
        return 'YES'
    return 'YES'

    

  for i in range(N):
    if A[i] == B[0]:
      break
  j = i
  i += 1
  i %= N
  k = 1
  while i != j:
    if A[i] != B[k]:
      return 'NO'
    k += 1
    i += 1
    i %= N
  return 'YES'


          
file1=open("consecutive_cuts_chapter_1_input.txt","r")
file2=open("consecutive_cuts_chapter_1_op.txt","w")

# Iterate over each line in the file
lineC = 0
caseC = 0
lines = file1.readlines()
# lines = [i for i in lines if i]
line = 1
while line < len(lines):
  lines[line] = lines[line].strip('\n')
  N, K = map(int, lines[line].split())
  A = []
  B = []
  for row in range(2):
    line += 1
    if row == 0:
      A = list(map(int,lines[line].split()))
    else:
      B = list(map(int,lines[line].split()))
  op = isItPossible(N, K, A, B)
  lineC += 1
  file2.write("{}{}{} {}".format("Case #", lineC, ":", str(op)))
  file2.write("\n")
  line += 1

    
# Release used resources
file1.close()
file2.close()
