def createStack():
  stack = []
  return stack

def isEmpty(stack):
  return len(stack) == 0
  
def push(stack, data):
  stack.append(data)
  print(str(data) + " is pushed into the stack")

def pop(stack):
  if(isEmpty()):
    return 'underflow'
  return stack.pop()

stack = createStack()
push(stack, 10)
push(stack, 20)

 

