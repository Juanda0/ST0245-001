class GraphAl:
    
	def __init__(self, size):
		self.size = size
		self.lista = [[] for i in range(size)]

	def getWeight(self, source, destination):
		for columna in self.lista[source]:
			if columna[0] == destination:
				return columna[1]

	def addArc(self, source, destination, weight):
			self.lista[source].append((destination, weight))

	def getSuccessors(self, vertice):
		succs = []
		for columna in self.lista[vertice]:
				succs.append(columna[0])
		return succs

class main:
  def main():
    a = GraphAl(8)

    a.addArc(0, 7,29)
    a.addArc(1, 2,27)
    a.addArc(3, 4,24)
    a.addArc(5, 6,32)
    a.addArc(7, 1,54)
    a.addArc(1, 3,36)
    a.addArc(4, 5,74)
    a.addArc(2, 3,12)
    a.addArc(1, 7,78) 
    #El metodo get edges lo usamos para retornar el codigo que genera el grafo en la pagina webgraphviz

    print(a.getWeight(0, 7))
    print(a.getSuccessors(1))

if __name__ == "__main__":
	main.main()
