def ways(n):
  if(n <= 2):
    return n
  return ways(n-1) + ways(n-2)
