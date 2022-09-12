


def secondHands(sArr, capacity, n):
  if n > (capacity*2):
    return 'NO'
  c = {}
  # c1Count = 0
  # c2Count = 0
  for num in sArr:
    if num not in c:
      c[num] = 1
    else:
      c[num] += 1
      if c[num] > 2:
        return 'NO'

  return 'YES'


file1=open("second_hands_input.txt","r")
file2=open("secondhandsop.txt","w")

# Iterate over each line in the file
lineC = 0
caseC = 0
for line in file1.readlines():
  line = line.strip('\n')
  lineC += 1
  if lineC != 1 and lineC %2 == 0 :
    N, K = map(int, line.split())
  elif lineC != 1 and lineC %2 != 0:
    arr = map(int, line.split())
    op = secondHands(arr, K, N)
    file2.write("{}{}{} {}".format("Case #", lineC//2, ":", str(op)))
    file2.write("\n")




    
# Release used resources
file1.close()
file2.close()