module = 1000000007
import math
def distanceCalc(N, Q, A, B):
  wholeDist = 0
  for well in B:
    wellDist = 0
    for tree in A:
      # tempDist = (math.pow(a, 2) + math.pow(b, 2))%module
      tempDist = ((((well[0]-tree[0])**2)%module) + (((well[1]-tree[1])**2)%module))%module
      wellDist = (tempDist%module+wellDist%module)%module
    wholeDist =(wholeDist%module + wellDist%module)%module
  return wholeDist

  
          
file1=open("watering_well_chapter_1_input.txt","r")
file2=open("watering_well_chapter_1_op.txt","w")

# Iterate over each line in the file
lineC = 0
caseC = 0
lines = file1.readlines()
# lines = [i for i in lines if i]
line = 1
while line < len(lines):
  lines[line] = lines[line].strip('\n')
  N = int(lines[line])
  A = []
  B = []
  for row in range(N):
    line += 1
    Ax, Ay = map(int, lines[line].split())
    A.append((Ax, Ay))
  line += 1
  Q = int(lines[line])
  for row in range(Q):
    line += 1
    Bx, By = map(int, lines[line].split())
    B.append((Bx, By))

  op = distanceCalc(N, Q, A, B)
  lineC += 1
  file2.write("{}{}{} {}".format("Case #", lineC, ":", str(op)))
  file2.write("\n")
  line += 1

    
# Release used resources
file1.close()
file2.close()
