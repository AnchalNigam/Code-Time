def repeatedNumber(self, A):
  dic = {}
  for idx,value in enumerate(A):
    if value not in dic:
        dic[value] = 1
    else:
        return value