# def powerset(x):
#   m = []
#   if not x:
#     m.append(x)
#   else:
#     A = x[0]
#     B= x[1:]
#     for z in powerset(B):
#       print(z, B, A, 'yss')
#       m.append(z)
#       r = [A] + z
#       print([A])
#       print(m)
#       m.append(r)
#   return m
# print(powerset([1,2,3,4]))
colors = [[1,1,1], [0,0,2], [5,0,0],[5,2,2]]
queries = [[5,1,3]]
# res = ['NO' for idx in range(len(queries))]
# from operator import itemgetter
# def sub_lists(l): 
#     base = []   
#     lists = [base] 
#     for i in range(len(l)): 
#         orig = lists[:] 
#         new = l[i] 
#         for j in range(len(lists)): 
#             lists[j] = lists[j] + [new] 
#         lists = orig + lists 
#     return lists 
# for subset in sub_lists(colors):
#   finalColor = []
#   if subset != []:
#     finalColor = [max(subset,key=itemgetter(0))[0], max(subset,key=itemgetter(1))[1], max(subset,key=itemgetter(2))[2]]
#     print(finalColor, subset,max(subset,key=itemgetter(0)) )
#     try:
#       ind = queries.index(finalColor)
#       res[ind] = 'YES'
#     except:
#       pass

# for value in res:
#   print(value)

