def plusOne(digits):
  for idx in range(len(digits)-1, -1, -1):
    flag = False
    if digits[idx] + 1 < 10:
      digits[idx] += 1
      break
    else:
      flag = True
      digits[idx] = 0
  if flag:
    digits.insert(0,1)
  return digits


