def createStacks():
  s1 = []
  s2 = []
  return s1, s2

def isEmpty(stack):
  return len(stack) == 0

def enqueue(s1, s2, data):
  if(not isEmpty(s1)):
    while len(s1) != 0:
      s2.append(s1[len(s1)-1])
      s1.pop()
  s1.append(data)
  while len(s2) != 0:
    s1.append(s2[-1])
    s2.pop()
  return s1, s2

    
def dequeue(s1):
  s1.pop()
  # print(s2)
  return s1

def printQueue(s1, s2):
  print(s1, 'print')
  for i in range(len(s1) - 1, -1, -1):
    print(s1[i])




s1, s2 = createStacks()
s1, s2 = enqueue(s1, s2, 1)
s1, s2 = enqueue(s1, s2, 2)
s1, s2 = enqueue(s1, s2, 3)
s1, s2 = enqueue(s1, s2, 4)
s1 = dequeue(s1)
s1 = dequeue(s1)
printQueue(s1, s2)


