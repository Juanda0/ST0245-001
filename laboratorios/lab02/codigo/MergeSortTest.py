""
import numpy as np
import time

def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 
        L = arr[:mid] 
        R = arr[mid:] 
  
        mergeSort(L) 
        mergeSort(R) 
  
        i = j = k = 0
        while i < len(L) and j < len(R): 
            if L[  i] < R[j]: 
                arr[k] = L[i] 
                i+= 1
            else: 
                arr[k] = R[j] 
                j+= 1
            k+= 1
        while i < len(L): 
            arr[k] = L[i] 
            i+= 1
            k+= 1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+= 1
            k+= 1
    
    
i = 100000
while i<=2000000:
    arr = np.random.randint(0, high = 100000,size=i)
    start_time = time.time()
    mergeSort(arr)  
    end_time = time.time()
    print('size:  '+ str(i))
    print('Time#'+ str(int(i/100000)) + ':  ' + str(end_time-start_time))
    i += 100000
    
