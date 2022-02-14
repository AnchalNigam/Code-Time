# def generateSubSets(nums):
#   res = []
#   def solve(nums, op):
#     if(len(nums) == 0):
#       res.append(op)
#       return
#     op2 = op.copy()
#     op2.append(nums[0])
#     solve(nums[1:], op)
#     solve(nums[1:], op2)
#   solve(nums, [])
#   return res

# a = [1,2,3]
# print(generateSubSets(a))
    
# https://www.youtube.com/watch?v=Yg5a2FxU4Fo

def generateSubSets(nums):
  res = []
  def solve(temp, index):
    print(index, 'index')
    res.append(temp[:])
    for i in range(index, len(nums)):
      # temp.append(nums[i])
      # print(temp, 'tempppp')
      # solve(index+1)
      # print(temp, 'temp2', index)
      # temp.pop(-1)
      temp.append(nums[i])
      print(temp, 'tempppp', i, nums)
      solve(temp, i+1)
      # print(temp+[nums[i]], 'temp2', index)
      print(temp, 'temp2')
      temp.pop()
    return
  solve([], 0)
  print(res, 'testtt') 


def anc():
  res = []
  temp = ['1']
  res.append(temp)
  solve(['2'], res)
  print(res, 'anchalllll')


def solve(temp, res):
  res.append(temp[:])
  for i in range(1):
    temp.pop()
# solve(['2'])
# print(res, 'anchalllll')

# anc()

nums = [1,2]
# print(a.subsets(nums))

print(generateSubSets(nums))


# in first approach, we are basically making two choices, including 1 and not including,
# if we include 1 then op update whereas op diff, we are maintaing both op and
# also update ip after that...


# a lot of learning here, in this pass by reference gyan i have got...here res is actually taken as
# reference and temp variable is also passed as reference so temp me alter gets altered in res variable
# as well because of referencing so to break referencing between temp and res, we appended copy 
# of temp, not temp...and then loop maintains temp which is referencing to same temp
# and in this wa, it worked

# https://leetcode.com/problems/subsets/discuss/27281/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)