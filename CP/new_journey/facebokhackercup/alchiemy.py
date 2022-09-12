


def alcheimyPossible(s, n):
  aCount = 0
  for char in s:
    if char == 'A':
      aCount += 1
  bCount = n-aCount

  return 'Y' if abs(aCount-bCount) == 1 else 'N'


file1=open("input.txt","r")
file2=open("output.txt","w")

# Iterate over each line in the file
lineC = 0
caseC = 0
for line in file1.readlines():
  line = line.strip('\n')
  lineC += 1
  if lineC != 1 and lineC %2 == 0 :
    N = int(line)
  elif lineC != 1 and lineC %2 != 0:
    op = alcheimyPossible(line, N)
    file2.write("{}{}{} {}".format("Case #", lineC//2, ":", str(op)))
    file2.write("\n")




    
# Release used resources
file1.close()
file2.close()