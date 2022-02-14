# def  decodeWays(s):
#   def _dp_helper(data, dp):
#     if not data:
#       return 1
#     first_call, second_call = 0, 0
#     if data in dp:
#       return dp[data]
#     if 1 <= int(data[:1]) <= 9:
#       first_call = _dp_helper(data[1:], dp)
#     if 10 <= int(data[:2]) <= 26:
#       second_call = _dp_helper(data[2:], dp)
#     dp[data] = first_call + second_call
#     return dp[data]
#   return _dp_helper(s, {})

# print(decodeWays("11106"))


def decodeways(s):
  result = [0]
  data = {}
  def solve(st, start, res):
    # print(res, start, 'hiii')
    if start < len(st) and st[start] == '0':
      return 
    if start >= len(st):
      result[0] += 1
      return
    if(st[start:start+1] and 1 <= int(st[start:start+1]) <= 9):
      res.append(st[start:start+1])
      # print(res, 'res')
      # result.append(st[start: start+1])
      solve(st, start+1, res)
      print(res, 'ji', start)
      res.pop()
 
    if(start+2 <= len(st) and int(st[start: start+2]) <=  26):
      res.append(st[start:start+2])
      # print(res, 'po')
      # result.append(st[start: start+2])
      solve(st, start+2, res)
      print(res, 'ji', start)
      res.pop()
  
    
  
  solve(s, 0, [])
  return result[0]


print(decodeways("226"))