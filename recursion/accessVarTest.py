# total = 0
# def recursive_me(mystring):
#     global total
#     chars = len(mystring)
 
#     if chars == 0:
#         print("Done")
#         # print(total[0])
#     else:      
#       first = int(mystring[0])
#       total = total + first
#       recursive_me(mystring[1:])

# recursive_me("4567")
# print(total)

# def sum_list_items(_list):
#     total = 0

#     def do_the_sum(_list):
#         for i in _list:
#             total += i

#     do_the_sum(_list)

#     return total

# sum_list_items([1, 2, 3])

c = 0
res = 0
def solve():
  global c
  print(c)

  if c < 8:
    print('hii')
  c += 2
  if c < 8:
    print('hii2')
solve()
