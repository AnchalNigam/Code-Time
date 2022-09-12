
def weakTyping(N, word):
  # print(word, 'word')
  lastChar = ""
  switch = 0
  for char in word:
    # print(char)
    if (lastChar == "") and (char == 'O' or char == 'X'):
      lastChar = char
    elif char != 'F' and lastChar != 'F' and lastChar != char:
      # print('inside')
      switch += 1
      lastChar = char
  return switch




file1=open("weak_typing_chapter_1_input.txt","r")
file2=open("weakTyping_op.txt","w")
# Iterate over each line in the file
lineC = 0
lines = file1.readlines()
# lines = [i for i in lines if i]
line = 1
while line < len(lines):
  lines[line] = lines[line].strip('\n')
  if line % 2 != 0:
    N = int(lines[line])
  else:
    op = weakTyping(N, lines[line])
    lineC += 1
    file2.write("{}{}{} {}".format("Case #", lineC, ":", str(op)))
    file2.write("\n")
  line += 1

    
# Release used resources
file1.close()
file2.close()
