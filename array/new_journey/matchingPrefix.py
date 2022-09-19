# from typing import List


# def matchingPrefix(n: int, arr: List[str]) -> str:
#     # write your code here
#     dic = {}
#     arr.sort()
#     p = arr[0]
#     ans = len(p)
#     y = p
#     print(arr)
#     for i in range(len(p)):
#         dic[p[0:i+1]] = 1
#     for i in range(1, len(arr)):
#         x = ""
#         print(arr[i],'-----')
#         for j in range(len(arr[i])):
#           z = arr[i][0:j+1]
#           if z not in dic:
#             dic[z] = 1
#           else:
#             dic[z] += 1
#         print(dic, 'bahar')

#         for j in range(len(p)):
#             if arr[i][j] == p[j]:
#                 print(p[j], 'lll')
#                 x += p[j]
#                 print(x, 'check')
#                 # if x not in dic:
#                 #     dic[x] = 1
#                 # else:
#                 #     dic[x] += 1
#                 print(dic, 'dicccc', ans, y, x)
               
#                 if x in dic and ans < dic[x] *(j+1):
#                   ans = dic[x] *(j+1)
#                   print(x, 'xxxxxxxxxxxxxxx', ans)
#                   y = x 
#                 elif x in dic and ans == dic[x] *(j+1) and x < y:
#                   print('andarrrr', x, y)
#                   y = x
#             else:
#                 print('break', x, ans, y, arr[i])
#                 break
#         # if x in dic and ans < dic[x] *(j):
                
#         #     ans = dic[x] *(j)
#         #     print(x, 'xxxxxxxxxxxxxxx', ans)
#         #     y = x 
#         # elif x in dic and ans == dic[x] *(j) and x < y:
#         #     print('andarrrr', x, y)
#         #     y = x
#         if ans < len(arr[i]):
#           y = arr[i]
#           ans = len(arr[i])
#           print('insides', ans, y)
#         elif ans == len(arr[i]) and x < y:
#           y = x
 
#         p = arr[i]

#     return y

# arr = ["abab",
# "bbbb",
# "b",
# "aa",
# "babaa",
# "a",
# "bb",
# "babb",
# "b",
# "abba"]   
arr = ["co",
"code",
"studio",
"codingninjas",
"coding",
"debug",
"coder",
"cipher"]
# # ['a', 'aaba', 'ba', 'baba', 'bb', 'bbab']   
dic = {}
for i in range(len(arr)):
  x = ""
  for j in range(len(arr[i])):
    x += arr[i][j]
    if x not in dic:
      dic[x] = 1
    else:
      dic[x] += 1
maxx = 0
ans = ""
for char in dic:
  if maxx < len(char)*dic[char]:
    ans = char
    maxx = len(char)*dic[char]
print(ans)
# time complexity would be o(n*l) - l is longest string in aray and n is array legth
# iteration is also in dif that would also be n*l times 
# space would also be same as n*l jo bhi max hga whi hm har string k man rhe hai
# so har string agr l size ki hue toh n*l hua na
#print(matchingPrefix(5, arr))



