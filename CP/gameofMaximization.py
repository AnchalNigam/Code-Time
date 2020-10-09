def maximumStones(arr):
  # Write your code here
  evenStones = 0
  oddStones = 0
  for idx in range(0, len(arr), 2):
      evenStones += arr[idx]
  for idx in range(1, len(arr), 2):
      oddStones += arr[idx]
  return sum(arr) - abs(evenStones - oddStones)
      