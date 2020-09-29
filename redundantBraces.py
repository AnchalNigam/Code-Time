def braces(A):
  stack = []
  operators = ["+", "-", "*", "/"]
  stack.append(A[0])
  for idx in range(1, len(A)):
    others = False
    if A[idx] == "(" or A[idx] in operators:
      stack.append(A[idx])
    elif A[idx] == ')' and len(stack) != 0:
      elem = stack.pop()
      while elem != "(":
        others = True
        elem = stack.pop()
      if not others:
        return 1
  isBracket = False
  if len(stack) != 0:
    for idx in stack:
      if idx == "(":
        isBracket = True
        break
  if len(stack) != 0  and not isBracket:
    return 0

  if len(stack) == 0 and others:
    return 0
  return 1

print(braces('(a+(b))'))



#different cases
# 1. there must be opeartors between open and close isBracket ( others variable handling this)
# 2. if there is no brackets at all (line n0 16 to 21 is responsible for handling this)
# 3. if len(stack) 0 and others bhi hai mns operator hai between brackets then no redundant brackets
