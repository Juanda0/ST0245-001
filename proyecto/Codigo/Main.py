
import Tree

def generateLista(dataset, lista):
  for i in range(len(dataset)):
      lista.append(i)

if __name__ == '__main__':

  #Arreglo contiene posiciones a testear
  posVariables = [9, 10, 13, 46, 47, 52, 53, 54, 55, 65, 66, 67,68,69,70,71,72,73,74,75,76]

  datasetTrain = Tree.ArbolDecision.leerDatos('4_train_balanced_135000.csv')
  datasetTest =  Tree.ArbolDecision.leerDatos('4_train_balanced_135000.csv')

  listaTrain = []
  listaTest = []
  
  generateLista(datasetTrain, listaTrain)
  generateLista(datasetTest, listaTest)

  bosque = []  
  #crear un solo arbol con todo el dataset:
  #arbolito = Tree.ArbolDecision(listaTrain, posVariables, datasetTrain, alturaMaxima = 10)
  #bosque.append(arbolito)
  
  #parametros para crear un bosque (El tamaño del arbol varia entre 10 a sizeArbol+10, y la altura
  #varia entre 3 y rangoAltura+3
  cantArboles = 1000
  sizeArbol = 20
  rangoAltura = 4
  #Testear 25000 datos tiene una duracion estimada de 230 segundos
  Tree.ArbolDecision.generarBosque(bosque, posVariables, datasetTrain, datasetTest, listaTest, listaTrain, cantArboles, sizeArbol, rangoAltura)
  
     





  