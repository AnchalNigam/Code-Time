def isPalindrome(string):
  def isPalin(string):
    if len(string) == 0:
      return ''
    elif len(string) == 1:
      return string[0]
    return string[len(string)-1] + isPalin(string[:len(string)-1])
  reverseStr = isPalin(string)
  print(reverseStr)
  if reverseStr == string:
    return True
  return False

print(isPalindrome('abba'))
