string = "gEEk"
dic = { 'c': 0, 's': 0 }
count = 0
for idx in range(len(string)-1):
  
  i = idx
  j = i
  subStr = ""
  while j < len(string):
    subStr += string[j]
    if string[j].isupper():
      dic['c'] += 1
    else:
      dic['s'] += 1
    if dic['c'] == dic['s']:
      count += 1
    j += 1
  dic = { 'c': 0, 's': 0 }
print(count)

    
