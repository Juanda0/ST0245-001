#!/usr/bin/python

import sys
import resource
resource.setrlimit(resource.RLIMIT_STACK,
                   [0x1000000000, resource.RLIM_INFINITY])
sys.setrecursionlimit(1000000000)
data = range(0, 10000000)

import os 
for size in range(1000000,20000000,1000000):     
  filename = "array-of-size-"+str(size)+".csv"     
  theFile = open(filename,"w")     
  for i in range(0,size):         
    if i == size-1:             
      theFile.write(str(i))         
    else:             
      theFile.write(str(i)+",")     
  theFile.close()     
  os.system("zip "+filename.replace("csv","zip")+" "+filename)     
  os.system("rm "+filename)

def arrayMax_aux(arr, i, max):
    if i == len(arr): 
        return max    
    else:
        if arr[i] > max:  
            max = arr[i]  
        return arrayMax_aux(arr, i + 1, max) 
        
print(arrayMax_aux(theFile, 0, theFile[0]))

def groupSum_aux(list, start, target):
    if start >= len(list): 
      return target == 0
    return groupSum_aux(list, start + 1, target - list[start]) \
            or groupSum_aux(list, start + 1, target)
print(groupSum_aux(theFile,0,14))

