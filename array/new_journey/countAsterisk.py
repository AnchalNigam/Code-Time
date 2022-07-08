count = 0
s = "yo|uar|e**|b|e***au|tifu|l"
isPairGoing = False
for char in s:
  if not isPairGoing  and char == "*":
    count += 1
  elif char == "|":
    isPairGoing = not isPairGoing
print(count)