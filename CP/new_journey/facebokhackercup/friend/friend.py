


def secondFriend(r, c, matrix):
  if r == 1 or c == 1:
    for i in range(r):
      for j in range(c):
        if matrix[i][j] == '^':
          return 'Impossible'

  return 'Possible'


file1=open("second_friend_input.txt","r")
file2=open("second_friend_output.txt","w")

# Iterate over each line in the file
lineC = 0
caseC = 0
lines = file1.readlines()
# lines = [i for i in lines if i]
line = 1
while line < len(lines):
  lines[line] = lines[line].strip('\n')
  R, C = map(int, lines[line].split())
  matrix = []
  for row in range(R):
    line += 1
    matrix.append(list(lines[line]))
  op = secondFriend(R, C, matrix)
  lineC += 1
  file2.write("{}{}{} {}".format("Case #", lineC, ":", str(op)))
  outputMatrix = []
  if op == 'Possible':
    file2.write("\n")
    char = ''
    if R == 1 or C == 1:
      char = '.'
    else: 
      char = '^'
    for i in range(R):
      file2.write(char*C)
      file2.write("\n")
  else:
    file2.write("\n")
  line += 1

# for line in file1.readlines():
#   line = line.strip('\n')
#   lineC += 1
#   if lineC != 1 and lineC %2 == 0 :
#     N, K = map(int, line.split())
#   elif lineC != 1 and lineC %2 != 0:
#     arr = map(int, line.split())
#     op = secondFriend(arr, K, N)
#     file2.write("{}{}{} {}".format("Case #", lineC//2, ":", str(op)))
#     file2.write("\n")




    
# Release used resources
file1.close()
file2.close()