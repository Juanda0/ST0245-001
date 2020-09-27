import collections

def atenderPorColas(q1, q2, q3, q4):
  i = 0  
  cajero1 = "Esta siendo Atendido por el Cajero1"
  cajero2 = "Esta siendo Atendido por el Cajero2"
  cajero = cajero1
  while(len(q1) != 0 or len(q2) != 0 or len(q3) != 0 or len(q4) != 0):
    if i == 0:
      if len(q1) != 0:
        print(q1.popleft() + " " + cajero)
        if cajero == cajero1:
          cajero = cajero2
        else:
          cajero = cajero1
      else:
        i += 1
    if i == 1:
      if len(q2) != 0:
        print(q2.popleft() + " " + cajero)
        if cajero == cajero1:
          cajero = cajero2
        else:
          cajero = cajero1
      else:
        i += 1
    if i == 2:
      if len(q3) != 0:
        print(q3.popleft() + " " + cajero)
        if cajero == cajero1:
          cajero = cajero2
        else:
          cajero = cajero1
      else:
        i += 1
    if i == 3:
      if len(q4) != 0:
        print(q4.popleft() + " " + cajero)
        if cajero == cajero1:
          cajero = cajero2
        else:
          cajero = cajero1
      i = -1
    i += 1

    
    


clientesQueue1 = collections.deque([])
clientesQueue1.append("Juan de la cola 1")
clientesQueue1.append("Pedro de la cola 1")
clientesQueue1.append("Roberto de la cola 1")
clientesQueue1.append("Emilio de la cola 1")


clientesQueue2 = collections.deque([])
clientesQueue2.append("Juan de la cola 2")
clientesQueue2.append("Pedro de la cola 2")
clientesQueue2.append("Roberto de la cola 2")


clientesQueue3 = collections.deque([])
clientesQueue3.append("Juan de la cola 3")
clientesQueue3.append("Pedro de la cola 3")
clientesQueue3.append("Roberto de la cola 3")
clientesQueue3.append("Emilio de la cola 3")
clientesQueue3.append("Pepe de la cola 3")
clientesQueue3.append("Pablo de la cola 3")


clientesQueue4 = collections.deque([])
clientesQueue4.append("Juan de la cola 4")
clientesQueue4.append("Pedro de la cola 4")


atenderPorColas(clientesQueue1, clientesQueue2, clientesQueue3, clientesQueue4)

#Para colas solo se usaron los metodos append y popleft, imitando el comportamiento de una cola y el metodo poll