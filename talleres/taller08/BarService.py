import collections

def barService(queue):
  auxQueue = collections.deque([])
  if len(queue) == 0: return
  while(len(queue) > 1):
    auxQueue.append(queue.pop())
  print("atendiendo a: " + queue.pop())
  while(len(auxQueue)>0):
    queue.append(auxQueue.pop())
  return barService(queue)

queue = collections.deque([])
queue.append('Juan')
queue.append('Maria')
queue.append('Pedro')
print(queue)
barService(queue)

#Solo se hizo uso de append y pop con el objetivo de simular 
#el funcionamiento de la cola
