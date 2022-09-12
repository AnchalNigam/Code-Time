
def morseCode(N, codeWord):
  nums = [".-", "-...", "-.-.",
                 "-..", ".", "..-.",
                 "--.", "....", "..",
                 ".---", "-.-", ".-..",
                 "--", "-.", "---", ".--.",
                 "--.-", ".-.", "...", "-",
                 "..-", "...-", ".--", "-..-",
                 "-.--", "--.."]

#   .-
# .--.
# -...
# .--.

  result = []
  def solve(start, res):
    if(len(result) >= N-1):
      return
    if(start >= 26):
      return
    if len(res) <= 200:
      # print(res, 'check')
      if codeWord != nums[start] and res != "":
        result.append(nums[start])
      res += nums[start]
      result.append(res)
      solve(start+1, res) 
    solve(start+1, res)

  solve(0, "")
  return result


file1=open("second_meaning_validation_input.txt","r")
file2=open("meaning_output.txt","w")

# Iterate over each line in the file
lineC = 0
caseC = 0
lines = file1.readlines()
# lines = [i for i in lines if i]
line = 1
while line < len(lines):
  lines[line] = lines[line].strip('\n')
  if line % 2 != 0:
    N = int(lines[line])
  else:
    op = morseCode(N, line)
    lineC += 1
    file2.write("{}{}{} ".format("Case #", lineC, ":"))
    file2.write("\n")
    for i in range(N-1):
      file2.write(''.join(op[i]))
      file2.write("\n")
  line += 1

    
# Release used resources
file1.close()
file2.close()
