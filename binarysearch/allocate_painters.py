
def paint(A, B, C):
      low = 0
      high = 0
      for idx in range(len(C)):
          C[idx] *= B
          high += C[idx]
      res = 0
      while low <= high:
          mid = low + ((high-low)//2)
          print(low, high, mid)
          if(isValidMinTime(mid, A, C)):
            res = mid
            high = mid - 1
          else:
            low = mid + 1
      return res
def isValidMinTime(minTimeToPaint, painters, C):
  painter = 1
  time = 0
  for idx in range(len(C)):
    time += C[idx]
    if (C[idx] > minTimeToPaint):
      return False
    if time > minTimeToPaint:
      painter += 1
      time = C[idx]
    if painter > painters:
      return False
  return True
# A =  [ 97, 26, 12, 67, 10, 33, 79, 49, 79, 21, 67, 72, 93, 36, 85, 45, 28, 91, 94, 57, 1, 53, 8, 44, 68, 90, 24 ]
# B = 26
A = 2
B = 5
C = [1, 10]
print(paint(A, B, C))

# here basically we have to paint all the boards. so here we have set diff times and testing whether
# that time is actually feasible in painting all boards or not
#  like first found mid , 27 is feasible to paint both boards. we got no as second board 
# needs 50unit[check line 23, it checks whether single board itself taking a lot time than mintime] 
# so we move ahead then checked, for 41 units, its also not feasible then so on. sometimes after
# adding all the board time by p1 can take more time thats why adding of time logic implemented,
# this way we found our answer