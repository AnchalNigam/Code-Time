valueArr = [ 377, 932, 309, 945, 440, 627, 324, 538, 539, 119, 83, 930, 542, 834, 116, 640, 659, 705, 931, 978, 307, 674, 387, 22, 746, 925, 73, 271, 830, 778, 574, 98, 513, 987, 291, 162, 637, 356, 768, 656, 575, 32, 53, 351, 151, 942, 725, 967, 431, 108, 192, 8, 338, 458, 288, 754, 384, 946, 910, 210, 759, 222, 589, 423, 947, 507, 31 ]
sortedValueArr = sorted(valueArr, reverse=True)
print(sortedValueArr)
weightArr = [ 14, 19, 1, 42, 13, 6, 11, 10, 25, 38, 49, 34, 46, 42, 3, 1, 42, 37, 25, 21, 47, 22, 49, 50, 19, 35, 32, 35, 4, 50, 19, 39, 1, 39, 28, 18, 29, 44, 49, 34, 8, 22, 11, 18, 14, 15, 10, 17, 36, 2, 1, 50, 20, 7, 49, 4, 25, 9, 45, 10, 40, 3, 46, 36, 44, 44, 24 ]
dic = {}
for idx, value in enumerate(valueArr):
  if value not in dic:
    dic[value] = weightArr[idx]
macWeightCapacity = 588
maxValue = float('-inf')
for idx in range(len(sortedValueArr)):
  value = sortedValueArr[idx]
  weight = dic[sortedValueArr[idx]]
  for idx2 in range(idx+1, len(sortedValueArr)):
    weight += dic[sortedValueArr[idx2]]
    value += sortedValueArr[idx2]
    print(weight, value, 'check')
    if weight <= macWeightCapacity:
      maxValue = max(maxValue, value)
    else:
      value = sortedValueArr[idx]
      weight = dic[sortedValueArr[idx]]
if maxValue == float('-inf'):
  print(valueArr[0])
print(maxValue)

