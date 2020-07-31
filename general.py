s = "anchal"
stack = []

def push(data):
  stack.append(data)

def popp():
  return stack.pop()


for word in s:
  push(word)

reverseStr = ""
while len(stack) != 0:
  reverseStr += popp()
print(reverseStr)