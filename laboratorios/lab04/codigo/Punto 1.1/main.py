import Bee 
import math 
import sys

class main:
  def main():
    bees = Bee.Bee.crearAbejasPorTxt("ConjuntoDeDatosCon1000000abejas.txt")
    instancia = Octree(bees)
    instancia.choque()
    return

class Nodo:
  def __init__(self, bees, mins, maxs):
    self.bees = bees
    self.mins = mins
    self.maxs  = maxs
    self.nodes = [None, None, None, None, None, None, None, None]
    
  def anadirHijo(self, nodo):
    self.nodes.append(nodo)
  
  def toStringss(self):
    for i in self.bees:
      print(i.toString())

class Octree:  
  def __init__(self, bees):
    self.arbol = Nodo(bees, Bee.Bee.getMins(bees), Bee.Bee.getMaxs(bees))
    self.choques = []
    midX = (self.arbol.mins[0] + self.arbol.maxs[0])/2
    midY = (self.arbol.mins[1] + self.arbol.maxs[1])/2
    midZ = (self.arbol.mins[2] + self.arbol.maxs[2])/2
    self.nuevosNodos(self.arbol, midX, midY, midZ) 
    
    
  def nuevosNodos(self, nodoPapa: Nodo, midX: float, midY: float, midZ: float):  
    if len(nodoPapa.bees) < 2:
      return None #0

    condition = magnitud(nodoPapa.mins, nodoPapa.maxs) 
    
    if (condition <=250):
      self.choques.append(nodoPapa.bees)
      return 0

    matriz1 = []
    matriz2 = []
    matriz3 = []
    matriz4 = []
    matriz5 = []
    matriz6 = []
    matriz7 = []
    matriz8 = []

    for bee in nodoPapa.bees:
      if bee.getLatitude() <= midX and bee.getLongitude() <= midY and bee.getAltitude() <= midZ:
        matriz1.append(bee)
      elif bee.getLatitude() <= midX and bee.getLongitude() <= midY and bee.getAltitude() >= midZ:
        matriz2.append(bee)
      elif bee.getLatitude() <= midX and bee.getLongitude() >= midY and bee.getAltitude() <= midZ:      
        matriz3.append(bee)
      elif bee.getLatitude() <= midX and bee.getLongitude() >= midY and bee.getAltitude() >= midZ:
        matriz4.append(bee)
      elif bee.getLatitude() >= midX and bee.getLongitude() <= midY and bee.getAltitude() <= midZ:
        matriz5.append(bee)
      elif bee.getLatitude() >= midX and bee.getLongitude() <= midY and bee.getAltitude() >= midZ:
        matriz6.append(bee)
      elif bee.getLatitude() >= midX and bee.getLongitude() >= midY and bee.getAltitude() <= midZ:
        matriz7.append(bee)
      elif bee.getLatitude() >= midX and bee.getLongitude() >= midY and bee.getAltitude() >= midZ:
        matriz8.append(bee)

    centro = (midX, midY, midZ)
    print("Soy el centro jejeje -----------")
    print(centro)
    print("\n\n")
    print("---------------------------------")
    noditosbb = [
      Nodo(matriz1, nodoPapa.mins, centro),
      Nodo(matriz2, (nodoPapa.mins[0], nodoPapa.mins[1], midZ), (midX, midY, nodoPapa.maxs[2])),
      Nodo(matriz3, (nodoPapa.mins[0], midY, nodoPapa.mins[2]), (midX, nodoPapa.maxs[1], midZ)),
      Nodo(matriz4, (nodoPapa.mins[0], midY, midZ), (midX, nodoPapa.maxs[1], nodoPapa.maxs[2])),
      Nodo(matriz5, (midX, nodoPapa.mins[1], nodoPapa.mins[2]), (nodoPapa.maxs[0], midY, midZ)),
      Nodo(matriz6, (midX, nodoPapa.mins[1], midZ), (nodoPapa.maxs[0], midY, nodoPapa.maxs[2])),
      Nodo(matriz7, (midX, midY, nodoPapa.mins[2]), (nodoPapa.maxs[0], nodoPapa.maxs[1], midZ)),
      Nodo(matriz8, centro, nodoPapa.maxs)
    ]

    for nodito in noditosbb:
      if(len(nodito.bees) == 0):
        return
      else:
        nodoPapa.anadirHijo(nodito)
        centroNodito = midEjes(nodito.mins, nodito.maxs)
        self.nuevosNodos(nodito, centroNodito[0], centroNodito[1], centroNodito[2])
    return 0

  def choque(self):     
    for bee in self.choques:
      print("Estas " + str(len(bee)) + " abejas chocan: ")
     #print(*bee, sep = "\n")
      

def mit(p1: float, p2: float)->float:
  return p1 + p2 / 2

def midEjes(m: tuple, M: tuple):
  if m is None or M is None:
    return None

  res = (mit(M[0], m[0]), mit(M[1], m[1]), mit(M[2], m[2]))
  return res

def magnitud(m: tuple, M: tuple):
  if m is None or M is None:
    return None
  Vx = M[0]-m[0]
  Vy = M[1]-m[1]
  Vz = M[2]-m[2]
  res = math.sqrt((Vx**2) + (Vy**2) + (Vz**2))
  
  print(res)
  print("\n\n")
  return res

sys.setrecursionlimit(900000000)
#rint(resource.getrlimit(resource.RLIMIT_STACK))
print (sys.getrecursionlimit())

if __name__ == "__main__":
	main.main()