A = input()
b = ""
for idx1 in range(len(A)):
  newString = list(A[0:idx1+1])
  repeatingChar = []
  isAllRepeatingchar = True
  while len(newString) != 0:
    char = newString.pop(0)
    if char not in newString and char not in repeatingChar:
      isAllRepeatingchar = False
      b += char
      break
    elif char not in repeatingChar:
      repeatingChar.append(char)
  if isAllRepeatingchar:
    b += '#'
    
print(b)

A = input()
b = ""
for idx1 in range(len(A)):
  newString = list(A[0:idx1+1])
  repeatingChar = []
  isAllRepeatingchar = True
  char = newString.pop(0)
  while(len(newString) > 0  and (char in newString or char in repeatingChar)):
    if char not in repeatingChar:
      repeatingChar.append(char)
    char = newString.pop(0)

  if char not in newString and char not in repeatingChar:
    b += char
    isAllRepeatingchar = False
  if isAllRepeatingchar:
    b += '#'
 
#  x#iiiiiiiiiiiiiiiiwwwwwwwwwwwwwwwwwwwwww
    
print(b)


A = input()
b = ""
dic = {}
queue = []
for char in A:
  isAllRepeatingchar = True
  if char not in dic:
    dic[char] = 1
  else:
    dic[char] += 1
  queue.append(char)
  while len(queue) != 0:
    if dic[queue[0]] == 1:
      isAllRepeatingchar = False
      b += queue[0]
      break
    else:
      queue.pop(0)

  if isAllRepeatingchar:
    b += '#'

  
  
 
#  x#iiiiiiiiiiiiiiiiwwwwwwwwwwwwwwwwwwwwww
    
print(b)