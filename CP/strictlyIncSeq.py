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
  for key in dic:
      if dic[key] == 1:
          uniqueElem.append(key)
  if len(uniqueElem) != len(arr) and len(uniqueElem)%2 == 0:
      return 'Second'
  return 'First'