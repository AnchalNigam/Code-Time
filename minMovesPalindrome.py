
a = "AACECAAAA"
# one way ..time is more
# def solve(A):
#   idx = 0
#   moves = 0
#   appendedStr = ""
#   newStr = A
#   while idx <= len(newStr)//2:
#     if newStr[idx] != newStr[len(newStr)-idx-1]:
#       appendedStr += newStr[len(newStr)-idx-1]
#       newStr = appendedStr + A
#       moves += 1
#     else:
#       idx += 1
#   print(newStr)
#   return moves


# print(solve(a))
# other way going on
# def solve(A):
#   idx = 0
#   moves = 0
#   appendedStr = ""
#   newStr = A
#   count = 0
#   while idx < len(newStr)//2:
#     if A[count] != A[len(A)-count-1]:
#       appendedStr += A[len(A)-idx-1]
#       newStr = appendedStr + A
#       moves += 1
#     else:
#       count += 1
#     idx += 1
#   print(newStr)
#   return moves


# print(solve(a))