import collections
def invertirPila(stack):
  stackAux  = collections.deque([])
  while(len(stack) > 0):
    stackAux.appendleft(stack.popleft())  
  return stackAux

stack = collections.deque([])
stack.appendleft(1)
stack.appendleft(2)
stack.appendleft(3)
print(stack)
stack = invertirPila(stack)
print(stack)

#Solo se hizo uso de appendleft y popleft con el objetivo de simular 
#el funcionamiento de la pila
