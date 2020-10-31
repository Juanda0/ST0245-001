import csv
import collections
#La insercion esta diseñada para funcionar ya sea con el nombre de los vertices o sin estos. Si desea retirar la lista de nombres o modificarla, el programa seguira funcionando. En caso de nombrar los vertices, la insercion se realiza con los nombres de estos. En caso contrario, se realiza en orden numerico de manera predeterminada
class main:
  def main():		
    my_file = "Arcos.txt"
    csv.register_dialect('skip_space', skipinitialspace=True)
    with open(my_file, 'r') as f:
      next(f)
      reader=csv.reader(f , delimiter=' ', dialect='skip_space')
      arcs = [[], [], []]
      for item in reader:
        arcs[0].append(item[0]) 
        arcs[1].append(item[1])
        arcs[2].append(item[2]) 
    
    vertices = arcs[0] + list(set(arcs[1]) - set(arcs[0]))
    a = GraphAl(len(vertices))
    a.nombrarVertices(vertices)
    for i in range(len(arcs[0])):
      sourceNode = arcs[0][i]
      destinationNode = arcs[1][i]
      weight = float(arcs[2][i])
      a.addArc(sourceNode, destinationNode, weight)
    a.getEdges()

    print(a.find_path_DFS('287291738', '3923685035'))
    print(a.find_path_BFS('287291738', '3923685035'))

class GraphAl:
  def __init__(self, size):
    self.size = size
    self.lista = [[] for i in range(size)]
    self.nombresVertices = []
    for i in range(len(self.lista)):
      self.nombresVertices.append(i)

  def getWeight(self, source, destination):
    for d in self.lista[source]:
      if d[0] == destination:
        return d[1]

  def addArc(self, sourceNode, destinationNode, weight = 1):
    source = self.nombresVertices.index(sourceNode)
    destination = self.nombresVertices.index(destinationNode)
    self.lista[source].append((destination, weight))

  def getSuccessors(self, vertice):
    succs = []
    for d in self.lista[vertice]:
      succs.append(d[0])
    return succs

  def nombrarVertices(self, nombresVertices):
    if len(nombresVertices) == len(self.lista):
      self.nombresVertices = nombresVertices
    else:
      print("Los nombres exceden el tamaño de la lista")


  def getEdges(self):
    print("digraph Matriz {")
    i = 0
    for j in self.lista:
      try:
        a = '\"' + str(self.nombresVertices[i]) + '\"'
        b = '\"' + str(self.nombresVertices[j[0][0]]) + '\"'
        print("  " + a + ' -> ' + b )         
        i += 1
      except:
          break
    print("}")
  
  def find_path_DFS(self, nodo_inicial, nodo_objetivo):
    nodoinit = self.nombresVertices.index(nodo_inicial)
    nodoobj = self.nombresVertices.index(nodo_inicial)
    return self.find_path_DFS_Aux(nodoinit, nodoobj)

  def find_path_DFS_Aux(self, nodo_inicial, nodo_objetivo,visitado = []):
    #Casos base
    try:
        visitado.index(nodo_inicial) 
        return False
    except:
        if nodo_inicial == nodo_objetivo:
            return True
    
        #Caso Recursivo
        for child in self.lista[nodo_objetivo]:
          if self.find_path_DFS(child, nodo_objetivo, visitado):
              return True
          visitado.append(child)
            
        return False
  
  def find_path_BFS(self, nodo_inicial, nodo_objetivo):
    nodoinit = self.nombresVertices.index(nodo_inicial)
    nodoobj = self.nombresVertices.index(nodo_inicial)
    return self.find_path_BFS_aux(nodoinit, nodoobj)

  def find_path_BFS_aux(self, nodo_inicial, nodo_objetivo, visitados = []):
    visitados.append(nodo_inicial)
    q = collections.deque()

    if nodo_inicial == nodo_objetivo:
      return True
  
    for child in visitados:
        q.append(child)
        
    while q.size() != 0:
      a = q.pop()
      return self.find_path_BFS(a, nodo_objetivo, visitados)
      
    return False

if __name__ == "__main__":
	main.main()