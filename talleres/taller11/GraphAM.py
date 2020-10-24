import numpy as np
#La insercion esta diseñada para funcionar ya sea con el nombre de los vertices o sin estos. Si desea retirar la lista de nombres o modificarla, el programa seguira funcionando. En caso de nombrar los vertices, la insercion se realiza con los nombres de estos. En caso contrario, se realiza en orden numerico de manera predeterminada
class main:
  def main():		
    a = GraphAm(12)
    nombresVertices = [2,3,5,7,8,9,10,11]
    a.nombrarVertices(nombresVertices)  

    a.addArc(3, 8)
    a.addArc(3, 10)
    a.addArc(5, 11)
    a.addArc(7, 8)
    a.addArc(7, 11)
    a.addArc(8, 9)
    a.addArc(11, 2)
    a.addArc(11, 9)
    a.addArc(11, 10) 
    print(a.getEdges())
    print(a.getSuccessors(11))

class GraphAm:
  def __init__(self, size):
    self.matriz = np.zeros((size, size))
    self.nombresVertices = []
    for i in range(len(self.matriz)):
      self.nombresVertices.append(i)
  
  def getEdges(self):
    print("digraph Matriz {")
    for i in range(len(self.matriz)):
      for j in range(len(self.matriz[i])):
        if self.matriz[i][j] != 0:
          a = '\"' + str(self.nombresVertices[i]) + '\"'
          b = '\"' + str(self.nombresVertices[j]) + '\"'
          print("  " + a + ' -> ' + b )
    print("}")
    return self.matriz

  def nombrarVertices(self, nombresVertices):
    if len(nombresVertices) == len(self.matriz):
      self.nombresVertices = nombresVertices
    else:
      print("Los nombres exceden el tamaño de la lista")
      
  def getWeight(self, sourceNode, destinationNode):
    source = self.nombresVertices.index(sourceNode)
    destination = self.nombresVertices.index(destinationNode)
    return self.getWeightAux(source, destination)

  def getWeightAux(self, source, destination):
    return self.matriz[source][destination]
	
  def addArc(self, sourceNode, destinationNode, weight = 1): 
    source = self.nombresVertices.index(sourceNode)
    destination = self.nombresVertices.index(destinationNode)
    self.addArcAux(source, destination, weight)
	  
  def addArcAux(self, source, destination, weight = 1):
    self.matriz[source][destination] = weight
	
  def getSuccessors(self, vertexName):
    vertex = self.nombresVertices.index(vertexName)
    return self.getSuccessorsAux(vertex)
  
  def getSuccessorsAux(self, vertex):
    succesors = []
    for i in range(len(self.matriz[vertex])):
      if self.matriz[vertex][i] != 0:
        succesors.append(self.nombresVertices[i])
    return succesors


if __name__ == "__main__":
	main.main()
