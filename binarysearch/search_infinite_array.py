low = 0
high = 1
target = 1
A = [0,0,0,1,1,1]
while A[high] < target:
  low = high
  high *= 2

# this is problem statement where u have to find first 1's in infiinite array
# first find that range, low high, this can be done using abovre cde
# thn first occurence of lement can be find out by decreaing low indices till then time 
# low<=high. and store when A[mid] = low, and then decrease 