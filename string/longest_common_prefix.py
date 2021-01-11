# 1st way

# def longestCommonPrefix(strs) -> str:
#   commonPrefix = ""
#   for idx1 in range(len(strs[0])):
#     commonPrefix += strs[0][idx1]
#     for idx2 in range(1, len(strs)):
#       if(len(strs[idx2]) < len(commonPrefix) or strs[idx2][:len(commonPrefix)] != commonPrefix):
#         if len(commonPrefix) == 1:
#           return ""
#         return commonPrefix[:len(commonPrefix)-1]
  
              
  
#   return commonPrefix
# 2nd way
def longestCommonPrefix(strs) -> str:
  commonPrefix = ""
  if(len(strs) == 0):
    return commonPrefix
  
  shortest_str = len(strs[0])
  for idx in range(1, len(strs)):
    if len(strs[idx]) < shortest_str:
      shortest_str = len(strs[idx])

  for idx1 in range(shortest_str):
    char = strs[0][idx1]
    for idx2 in range(1,len(strs)):
      if strs[idx2][idx1] != char:
        return commonPrefix
    commonPrefix += char
  return commonPrefix


print(longestCommonPrefix(["a"]))