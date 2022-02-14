# think of recursion first, 123 , pair friends in party, 1 can be single or paired with 2
# or 3 ,  so end result me 
# 1 2 3
# 1 [2,3]
# 2 [1,3]
# 3 [1,2]

# so 1 is basically including in above. so, here now think for 1 ip i.e 1..1 k options explore krte h
# 1 akele, then 12 ek sath and 13 ek sath...then ab bacha hua explore kro...
def solve(out, n, counter):
  res = []
  def pairParty(out, ip, counter):
    print(ip, 'kya')
    counter += 1
    if counter == 3:
      return
    if len(ip) == 0:
      print('yes', out)
      return
    # out += '-' + ip[0]
    print(ip)
    res.append(out)
    for i in range(len(ip)):
      for j in range(len(ip)):
        pairParty(out+ '*' + ip[0], ip[1:], counter)
        if i != j:
          pairParty(out+ '*' + ip[i] + '*' + ip[j], ip[:i]+ip[i+1:j]+ip[j+1:], counter)
  pairParty( "", "12", 0)
print(solve( "", "12", 0))

