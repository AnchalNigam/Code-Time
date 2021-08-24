# mOrre voting algo
arr = [ 1, 1, 1, 2, 3, 5, 7 ]
# arr = [1,1,1,3,3,2,2,2]
m1 = -1
c1 = 0
m2 = -1
c2 = 0
for idx in range(len(arr)):
  if m1 == arr[idx]:
    c1 += 1
  elif m2 == arr[idx]:
    c2 += 1
  elif c1 == 0:
    m1 = arr[idx]
    c1 = 1
  elif c2 == 0:
    m2 = arr[idx]
    c2 = 1
  else:
    c2 -= 1
    c1 -= 1
c1 = 0
c2 = 0
print(m1)
for idx in range(len(arr)):
  if arr[idx] == m1:
    c1 += 1
  elif arr[idx] == m2:
    c2 += 1
  if c1 > len(arr)//3:
    print(m1)
  elif  c2 > len(arr)//3:
    print(m2)
print(-1)

  

# if n/3 saying = 8/3 -> > n/3 means greater thsan 8/3 = 2 + 1 ie 3 or more . 
# suppose array length is 8 then it means [0,0,0,0,0,0,0] then means 2 elements can be majority 
# or 1 or none. as first 3 space is occupied by 1 element then next is by another element.
# whereas in n/2 = 8/2 -> > n/2 means greater than 4 i.e 5 or more
# it means only 1 element can come..fist 5 can occupied by 1 element and none can repeate more than
# 5. so in case of n/3 then 2 elements can come then for n/2 then only one can come. 