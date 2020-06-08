def createStacks():
  s1 = []
  s2 = []
  return s1, s2

def isEmpty(stack):
  return len(stack) == 0

def enqueue(s1, data):
  s1.append(data)
  return s1

def dequeue(s1, s2):
  if(isEmpty(s2) and isEmpty(s1)):
    print('underflow')
  if(isEmpty(s2)):
    while(len(s1) != 0):
      s2.append(s1[-1])
      s1.pop()
  s2.pop()
  return s1, s2

def printQueue(s1, s2):
  for i in range(len(s2) - 1, -1, -1):
    print(s2[i])




s1, s2 = createStacks()
s1 = enqueue(s1, 1)
s1 = enqueue(s1, 2)
s1 = enqueue(s1, 3)
s1 = enqueue(s1, 4)
s1, s2 = dequeue(s1, s2)
s1, s2 = dequeue(s1,s2)
printQueue(s1, s2)


