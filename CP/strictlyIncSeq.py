def whoIsTheWinner(arr):
  # WRITE DOWN YOUR CODE HERE
  arr.sort()
  dic = {}
  for idx,value in enumerate(arr):
    if value not in dic:
      dic[value] = 1
    else:
      dic[value] += 1
  uniqueElem = []
  maxVal = float('-inf')
  for key in dic:
    if dic[key] == 1:
      uniqueElem.append(key)
    if dic[key] > maxVal:
      maxVal = dic[key] 
  
  if len(uniqueElem) != len(arr):
    if maxVal%2 != 0:
      if len(uniqueElem)%2 == 0:
        return 'First'
      return 'Second'
    else:
      if len(uniqueElem)%2 == 0:
        return 'Second'
      return 'First'
  return 'First'
print(whoIsTheWinner([1,2,2,3]))