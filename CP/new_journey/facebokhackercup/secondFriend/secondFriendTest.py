

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

def helper(i, j, row, col, resMatrix, matrix):
  if(i < 0 or j < 0 or i >= row or j >= col):
    return False
  if resMatrix[i][j] == '*' or matrix[i][j] == '#':
    return True
  if not isValid(i, j, row, col, matrix):
    return False
  resMatrix[i][j] = '*'
  # print(i, j)
  res1 = helper(i, j+1, row, col, resMatrix, matrix)
  res2 = helper(i, j-1, row, col, resMatrix, matrix)
  res3 = helper(i+1, j, row, col, resMatrix, matrix)
  res4 = helper(i-1, j, row, col, resMatrix, matrix)
  # print(res1, res2, res3, res4)
  c = 0
  if res1:
    c += 1
  if res2:
    c += 1
  if res3:
    c += 1
  if res4:
    c += 1
  if c >= 2:
    resMatrix[i][j] = '^'
    return True
  resMatrix[i][j] = '*'
  return False




# def secondFriend(r, c, matrix):
#   resMatrix = [row[:] for row in matrix]
#   for i in range(r):
#     for j in range(c):
#         if matrix[i][j] == '^':
#           # print(matrix[i][j], i, j,r,c, 'initial')
#           if(not helper(i, j, r, c, resMatrix, matrix)):
#             return 'Impossible', matrix

#   return 'Possible', resMatrix      
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
          

# def helper(i, j, row, col, resMatrix, first, matrix):
#   print(i, j, first, 'ppppppppppp')
#   print('++++++++++++++++++++')
#   c = 0
#   if i-1 >= 0 and matrix[i-1][j] != '#':
#     if first:
#       if(helper(i-1, j, row, col, resMatrix, False,matrix)):
#         resMatrix[i-1][j] = '^'
#         c += 1
#     c += 1
#   if i+1 < row and matrix[i+1][j] != '#':
#     if first:
#       if(helper(i+1, j,row, col, resMatrix, False, matrix)):
#         resMatrix[i+1][j] = '^'
#         c += 1
#     c += 1
#   if j+1 < col and matrix[i][j+1] != '#':
#     print(i, j, first, 'llllllllllllll')
#     if first:
#       if(helper(i, j+1,row, col, resMatrix, False, matrix)):
#         resMatrix[i][j+1] = '^'
#         c += 1
#     c += 1
#   if j-1 >= 0 and matrix[i][j-1] != '#':
#     if first:
#       if(helper(i, j-1, row, col, resMatrix, False, matrix)):
#         print(i, j, first, 'inside')
#         print('**************')
#         resMatrix[i][j-1] = '^'
#         c += 1
#     c += 1
#   if c < 2:
#     return False
#   print(i, j, first, resMatrix, 'end')

#   return True

# def secondFriend(r, c, matrix):
#   if r == 1 or c == 1:
#     for i in range(r):
#       for j in range(c):
#         if matrix[i][j] == '^':
#           return 'Impossible', matrix
#     return 'Possible', matrix
#   resMatrix = [row[:] for row in matrix]
#   for i in range(r):
#     for j in range(c):
#       countPossibility = 0
#       if matrix[i][j] == '^':
#         if i-1 >= 0 and matrix[i-1][j] != '#':
#           resMatrix[i-1][j] = '^'
#           countPossibility += 1
#         if i+1 < r and matrix[i+1][j] != '#':
#           resMatrix[i+1][j] = '^'
#           countPossibility += 1
#         if j+1 < c and matrix[i][j+1] != '#':
#           resMatrix[i][j+1] = '^'
#           countPossibility += 1
#         if j-1 >= 0 and matrix[i][j-1] != '#':
#           resMatrix[i][j-1] = '^'
#           countPossibility += 1
#         if countPossibility < 2:
#           return 'Impossible', matrix
#       else:
#         # if matr
#         resMatrix[i][j] = matrix[i][j]
#       print('==================')
#       print(resMatrix, 'each', i, j, matrix[i][j])


#   return 'Possible', resMatrix


file1=open("second_second_friend_sample_input.txt","r")
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
