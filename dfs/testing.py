def rec(x):
  temp = 0
  print(x, temp, 'oooW')
  for i in range(0, x):
    temp += 1
    print(x, temp, i)
    rec(i)
  print(temp, 'jajja')

rec(2)
# what i learnt is if you are running a loop and doing recursion then inside variable
# temp if you change in one loop then it would go same value like temp 1 rhega jab loop ka agla element
# ayega , if again apne temp+1 kia mns ab temp2 hai and ye testre element loop me bhi 2 rhega temp
# ka value so loop me inside var j bhi badal rhe h that would maintain (that will not get
# reste to 0 because outside temp hmne 0 set kia h so ye mat socho , loop me maintain rhta
# hai temp ka value)

# see n array depth question there also same itutation that har level k neche wale
# children k calculate krna ar dekhna k kiska depth max hai
# toh loop me chaleag depth update krte jao and  dekho har children me
# max(depth, solve(child)) so visualize yye kro-
# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
# frst eg ka visualize kro
# jab 5 pe hai toh depth 1 hga and fr 6 jab ayega toh depth is now 1 ..so compare
# hga max(1, solve(child)) - solve(child) will give 1 so depth 1 h gya kyunki depth=0 hmne define
# kia hai toh ab depth+1 hga toh depth=0 har level k children k lie reset h rha hai
# and comparisoon uske level k depth and uske apne calculated depth se h rha hai
# now dusre loop 3 wala chal rha hai that would give depth as 3 toh ab 2 ka apna
# apna depth , depth=0 hai toh depth+1 se 1 ayega ab j 3 same level pe h
# uske depth and 2 k depth me comparisoon hga so same level k depth k sath compaisoon
# and khud k depth ka calc, depth=0 se h rha hai
# 
# arg ap depth params me pass kroge toh apke depth add on hte jaega ar wo nodes ka count de dega
# because wo solve(child)(2) k jaise krega toh wo depth j already calculated hte usme +1
# krta hai naki apna depth maintain krta (depth=0 se wo h rha tha) tph ye pure feeling h 