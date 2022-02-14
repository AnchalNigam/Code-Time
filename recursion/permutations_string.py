# def permutationsInString(s1, s2):
#   # result = []
# def permutations(s1):
#   n = len(s1)
#   result = []
#   def solve(s1, res):
#     print(s1, res)
#     if len(s1) == 0:
#       result.append(res)
#       return
#     for i in range(len(s1)):
#       solve(s1[:i]+s1[i+1:],res+s1[i])
#   solve("abc", "")
#   return result



def permutationsInString(s1, s2):
  k = len(s1)
  dic = {}
  for i in range(k):
    if s1[i] not in dic:
      dic[s1[i]] = 1
    else:
      dic[s1[i]] += 1
  for i in range(len(s2)-k+1):
    tempS = s2[i:i+k]
    j = 0
    flag = True
    dic2 = {}
    for j in range(k):
      if tempS[j] not in dic:
        flag = False
        break
      if tempS[j] not in dic2:
        dic2[tempS[j]] = 1
      else:
        dic2[tempS[j]] += 1
    if flag:
      flag2 = True
      for l in dic:
        if l not in dic2:
          flag2 = False
          break
        elif l in dic2 and dic[l] != dic2[l]:
          flag2 = False
          break
      if flag2:
        return True
  return False
      
      

s1="ab"
s2="eidbaooo"
print(permutationsInString(s1,s2))



