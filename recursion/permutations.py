


def permutations(nums):
  result = []
  def solve(res, ip):
    if len(ip) == 0:
      result.append(res[:])
      return

    for i in range(len(ip)):
      solve(res+[ip[i]], ip[:i]+ip[i+1:])
    return
  solve([], nums)
  return result

print(permutations([1,2,3]))

# Time Complexity: O(n*n!) The time complexity is the same as the above approach, i.e. there are n! permutations and it requires O(n) time to print a permutation.

# Auxiliary Space: O(|s|)

# n! as a each level 1 number from array is reducing like in permutn - 4*3*2*1
# and at each level we are loopoing in that ip array so n . so overall- n*n!