

# ..^.
# .#^#
# ....
# ...^


def isValid(i, j, row, col, matrix):
  c = 0
  if i-1 >= 0 and matrix[i-1][j] != '#':
    c += 1
  if i+1 < row and matrix[i+1][j] != '#':
    c += 1
  if j+1 < col and matrix[i][j+1] != '#':
    c += 1
  if j-1 >= 0 and matrix[i][j-1] != '#':
    c += 1
  if c < 2:
    return False
  return True


def secondFriend(r, c, matrix):
  resMatrix = [row[:] for row in matrix]
  for i in range(r):
    for j in range(c):
      if matrix[i][j] == '.':
        if isValid(i, j, r, c, matrix):
          resMatrix[i][j] = '^'
        else: 
          matrix[i][j] = '#'
      elif matrix[i][j] == '^':
        if not isValid(i, j, r, c, matrix):
          return 'Impossible', matrix
  return 'Possible', resMatrix
          
file1=open("second_second_friend_input.txt","r")
file2=open("second_second_friend_output.txt","w")

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
  op, output = secondFriend(R, C, matrix)
  lineC += 1
  file2.write("{}{}{} {}".format("Case #", lineC, ":", str(op)))
  if op == 'Possible':
    file2.write("\n")
    for i in range(R):
      file2.write(''.join(output[i]))
  else:
    file2.write("\n")
  line += 1

    
# Release used resources
file1.close()
file2.close()
