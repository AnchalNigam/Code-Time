def excelSheetColNum(colTitle):
  n = len(colTitle)-1
  ans = 0
  for i in range(n, -1, -1):
    if (n-i) != 0:
      ans += (ord(colTitle[i])-64) * (pow(26, (n-i)))
    else:
      ans += (ord(colTitle[i])-64) 


  return ans
print(excelSheetColNum('ZY'))


