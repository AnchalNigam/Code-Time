


# Python program for KMP Algorithm
def KMPSearch(pat, txt):
  M = len(pat)
  N = len(txt)
  flag = False
  # create lps[] that will hold the longest prefix suffix
  # values for pattern
  lps = [0]*M
  j = 0
  # Preprocess the pattern (calculate lps[] array)
  computeLPSArray(pat, M, lps)

  i = 0 # index for txt[]
  while i < N:
    if pat[j] == txt[i]:
      i += 1
      j += 1

    if j == M:
      print ("Found pattern at index", str(i-j))
      flag = True
      j = lps[j-1]

    # mismatch after j matches
    elif i < N and pat[j] != txt[i]:
      # Do not match lps[0..lps[j-1]] characters,
      # they will match anyway
      if j != 0:
        j = lps[j-1]
      else:
        i += 1
  return flag

def computeLPSArray(pat, M, lps):
	len = 0 # length of the previous longest prefix suffix

	lps[0] # lps[0] is always 0
	i = 1

	# the loop calculates lps[i] for i = 1 to M-1
	while i < M:
		if pat[i]== pat[len]:
			len += 1
			lps[i] = len
			i += 1
		else:
			# This is tricky. Consider the example.
			# AAACAAAA and i = 7. The idea is similar
			# to search step.
			if len != 0:
				len = lps[len-1]

				# Also, note that we do not increment i here
			else:
				lps[i] = 0
				i += 1


# This code is contributed by Bhavya Jain

 
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

    
  AStr = ''.join(map(str, A))
  BStr = ''.join(map(str, B))
  txt = AStr + AStr
  pat = BStr
  if KMPSearch(pat, txt):
    return 'YES'
  return 'NO'



          
file1=open("consecutive_cuts_chapter_2_input.txt","r")
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
