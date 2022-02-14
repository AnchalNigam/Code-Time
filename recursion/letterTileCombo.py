

# def tile(s):
#   count = [0]
#   final = []
#   visited = {}
#   def combination(s):
#     # print(s, 'll')
#     result = []
#     def solve(start, res):
#       if start == len(s):
#         # print(visited, s, 'checking')
#         if res not in visited and res != '':
#           visited[res] = True
#           result.append(res)
#         return
    
#       res += s[start]
#       # print(start, res, 'check')
#       solve(start+1, res)
#       res = res[:-1]
#       solve(start+1, res)
#       # print(res, 'res')
#     solve(0, '')
#     return result
#   def perm(s, res, visit):
#     if len(s) == 0:
#       resStr = ''.join(map(str, res))
#       try:
#         if not visit[resStr]:
#           visit[resStr] = True
#       except KeyError:
#         r = combination(resStr)
#         final.append(r)
#         count[0] += len(r)
#         visit[resStr] = True
#       return
   
#     for i in range(len(s)): 
#       if(i>0 and s[i] == s[i-1] and not visit[s[i-1]]):
#         continue
#       visit[s[i]] = True   
#       perm(s[:i]+s[i+1:], res+s[i], visit)
#       visit[s[i]] = False

     
#   perm(s, '', {})
#   print(final, count)
def tile(tiles):
  res = set()
  def dfs(path, t):
    print(path)
    if path:
        res.add(path)
    for i in range(len(t)):
        dfs(path+t[i], t[:i] + t[i+1:])
          
  dfs('', tiles)
  return res
print(tile("ABC"))