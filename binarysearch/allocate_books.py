# def books(A, B):
#       low = 0
#       high = 0
#       for idx in range(len(A)):
#           high += A[idx]
#       n = 0
#       res = -1
#       if B > len(A):
#         return -1
#       while low <= high:
#           mid = low + ((high-low)//2) n*m log(sum of pages)
#           k = 0
#           n = 0
#           while k < B:
#               pages = 0
#               while n < len(A):
#                   pages += A[n]
#                   if pages > mid:
#                       k += 1
#                       break
#                   else:
#                       n += 1
#               if n >= len(A):
#                 break
                 
#           if n < len(A):
#               low = mid + 1
#           else:
#               res = mid
#               high = mid - 1
#       return res
# A =  [ 12, 34, 67, 90 ]
# B = 2
# print(books(A, B))
def books(A, B):
      low = 0
      high = 0
      for idx in range(len(A)):
          high += A[idx]
      res = -1
      if B > len(A):
        return -1
      while low <= high:
          mid = low + ((high-low)//2)
          if(isValidMinPage(mid, A, B)):
            res = mid
            high = mid - 1
          else:
            low = mid + 1
      return res
def isValidMinPage(minPagesToDistribute, books, students):
  student = 1
  pages = 0
  for idx in range(len(books)):
    pages += books[idx]
    if (books[idx] > minPagesToDistribute):
      return False
    if pages > minPagesToDistribute:
      student += 1
      pages = books[idx]
    if student > students:
      return False
  return True
# A =  [ 97, 26, 12, 67, 10, 33, 79, 49, 79, 21, 67, 72, 93, 36, 85, 45, 28, 91, 94, 57, 1, 53, 8, 44, 68, 90, 24 ]
# B = 26
A = [12, 34, 67, 90]
B = 2
print(books(A, B))

# both the sol works
# here the logic is instead of making combinations and seeing whch max student pages is minimum.
# we take out min pages by having low=0 and high=sum of pages and mid is basically min pages
# that we want to distribute. its basically whether its feasible to distribute that pages 
# among students or not. suppose 101 pages u want to distribute, you give student1 first two array
# then second student got 67 pages book and now 90 book is left that means book is left means
# to accumulate all books, we should inc min pages that means low would be mid+1 then one case is
# scheme is valid means that min pages is distributed among all students so this could be answer
# but we have to minimum so we decrease those min pages(high-1) then again we check whether this
# scheme is valid or not. if yes then again dec.if not meaning, we should inc min pages so that
# all students get some books. here time complexity is n*log(sumofpages). n is num of books
# line 56 is imp. see when books pages is more than min pages that means that no student will get that book
# so scheme fails as each student should get some book either 1 or more