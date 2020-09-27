def choosePivot(dataArray):
  pivot = 0
  condition = abs(sumArray(dataArray[:pivot]) - sumArray(dataArray[pivot+1:]))
  bestPivot = None
  while pivot < len(dataArray):
    conditionAux = abs(sumArray(dataArray[:pivot]) - sumArray(dataArray[pivot+1:]))
    if conditionAux <  condition:
      bestPivot = pivot
      condition = conditionAux
    pivot += 1
  return bestPivot

def sumArray(dataArray):
  total = 0
  for element in dataArray:
    total += element
  return total

test = [10,2,5,2,11]
print("The best pivot is in the position: " + str(choosePivot(test)))