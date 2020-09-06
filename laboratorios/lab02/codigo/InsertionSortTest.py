import time

def insertion_Sort(arr): 
  for i in range(1, len(arr)):
    aq = arr[i]
    j = i-1
    while j >= 0 and aq < arr[j]:
      arr[j+1] = arr[j] 
      j -= 1
    arr[j+1] = aq 
  print ("Filled list") 



i = 1000
while i<=20000:
    j = i
    c = 0
    arr = []
    while j >= 0:
        arr.append(j)
        j -= 1
        c += 1    
    start_time = time.time()
    insertion_Sort(arr)  
    end_time = time.time()
    print('Time#'+ str(int(i/1000)) + ':  ' + str(end_time-start_time))
    i += 1000
