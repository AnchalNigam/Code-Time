def countVowelStrings(n):
  vowels = ['a', 'e', 'i', 'o', 'u']    
  results = []
  helper(vowels, n, results, "", 0)
  # print(results, 'results')
  return len(results)
  
        
def helper(vowels, n, results, combination, start):
  print(results, combination, start, 'test')
  if len(combination) == n:
    results.append(combination)
    return
  
  for i in range(start, len(vowels)):
    c = vowels[i]
    
    combination += c
    
    helper(vowels, n, results, combination, i)
    
    combination = combination[:-1]

print(countVowelStrings(3))