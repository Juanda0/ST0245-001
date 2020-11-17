import csv
import Node
import time
import Giny
from secrets import randbelow
class ArbolDecision:  
# #Imprimime la condicion con menor impureza
# print("La impureza ponderada es: " + str()

# print("\n \n")
  def __init__(self, lista, posVariables, dataset, pregunta = None, altura = 0, alturaMaxima = 10):
    #print(str(posVariables) + "         " + str(altura))
    self.altura = altura
    self.dataset = dataset
    self.root = Node.node(lista)
    self.posVariables = posVariables.copy()
    self.impureza = Giny.giniImpurity.ginyImpurity(self.dataset, self.root.lista)
    if self.root.lista is None or len(self.posVariables) == 0 or self.impureza == 0 or self.altura == alturaMaxima:
      return

    self.nodos = self.dividirNodoMejorCondicion(self.root.lista, self.posVariables)
    
    
    self.pregunta = self.nodos[1]
    self.posVariables.remove(self.pregunta[0])

    #El print comentado genera un codigo que permite visualizar el arbol en webgrapgviz (no usar si se generan bosques)
    try: 
      self.root.leftNode = ArbolDecision(self.nodos[0][0], self.posVariables, dataset, altura = self.altura+1, alturaMaxima = alturaMaxima)
      #print(f'\t"{Giny.giniImpurity.porcentajeDeExito(self.dataset, self.root.lista)}     {self.altura}" -> "{Giny.giniImpurity.porcentajeDeExito(self.dataset,self.root.leftNode.root.lista)}     {self.root.leftNode.altura}"\n')
    except:
      self.root.leftNode = None  
        
    try:
      self.root.rightNode = ArbolDecision(self.nodos[0][1], self.posVariables, dataset, altura = self.altura+1, alturaMaxima = alturaMaxima)
      #print(f'\t"{Giny.giniImpurity.porcentajeDeExito(self.dataset, self.root.lista)}     {self.altura}" -> "{Giny.giniImpurity.porcentajeDeExito(self.dataset, self.root.rightNode.root.lista)}     {self.root.rightNode.altura}"\n')
    except:
      self.root.rightNode = None
    
    
  #Procesa el dataset  
  def leerDatos(archivo):
    with open(archivo, newline='', encoding="utf-8") as csvfile:
      reader = csv.reader(csvfile, delimiter=';')
      next(reader)
      data = []
      for row in reader:
        data.append(row)
      
    return data

  #Busca el primer valor existente de una variable para saber si es numerica o string
  def getPrimerValor(self, posVariable):
    i = 0
    #Si el primero es vacio, busca el primer valor en la lista con un valor real
    primero = self.dataset[i][posVariable]
    for fila in self.dataset:
      if primero == "":
        i += 1
        primero = self.dataset[i][posVariable]      
      else:
        break     
    return primero

  #divide una lista de acuerdo a una condicion
  #calcula la condicion que mejor reduce la impureza de una columnna
  def MejorVariable(self, lista, posVariable): 
    primero = self.getPrimerValor(posVariable)
    diccionarioVariables = {}
    for fila in lista:
      valor = self.dataset[fila][posVariable] 

      if diccionarioVariables.get(valor) is None:
        diccionarioVariables[valor] = [0,0]
        
      if int(self.dataset[fila][77]) == 1:
        diccionarioVariables[valor][0] += 1
      else:
        diccionarioVariables[valor][1] += 1
    #Si es un flotante
    try:
      float(primero) 
      minimaPonderada = 1
      minimoValor = ""
      for valor in diccionarioVariables:
        if valor == "":
          continue
        variable1 = [0,0]
        variable2 = [0,0]
        for valor2 in diccionarioVariables:
          if float(valor) > float(valor2):
            variable1[0] += diccionarioVariables[valor2][0]
            variable1[1] += diccionarioVariables[valor2][1]
          else:
            variable2[0] += diccionarioVariables[valor2][0]
            variable2[1] += diccionarioVariables[valor2][1]
        impureza1 = (Giny.giniImpurity.ginyImpurityAux(self.dataset, variable1[0], variable1[1]), variable1[0] + variable1[1])
        impureza2 = (Giny.giniImpurity.ginyImpurityAux(self.dataset, variable2[0], variable2[1]), variable2[0] + variable2[1])
        ponderada = Giny.giniImpurity.ginyImpurityWeightenedAux(self.dataset, impureza1[1], impureza2[1], impureza1[0], impureza2[0])

        if ponderada < minimaPonderada:
          minimaPonderada = ponderada
          minimoValor = valor
      return [minimaPonderada,minimoValor, posVariable]
    #Si es un String
    except:
      minimaPonderada = 1
      minimoValor = ""
      for valor in diccionarioVariables:
        if valor == "":
          continue
        variable1 = diccionarioVariables[valor]
        variable2 = [0,0]
        for valor2 in diccionarioVariables:
          if valor != valor2:
            variable2[0] += diccionarioVariables[valor2][0]
            variable2[1] += diccionarioVariables[valor2][1]

        impureza1 = (Giny.giniImpurity.ginyImpurityAux(variable1[0], variable1[1]), variable1[0] + variable1[1])
        impureza2 = (Giny.giniImpurity.ginyImpurityAux(variable2[0], variable2[1]), variable2[0] + variable2[1])
        ponderada = Giny.giniImpurity.ginyImpurityWeightenedAux(impureza1[1], impureza2[1], impureza1[0], impureza2[0])

        if ponderada < minimaPonderada:
          minimaPonderada = ponderada
          minimoValor = valor
      return [minimaPonderada,minimoValor, posVariable]
    
  def dividirNodoMejorCondicion(self, lista, listaVariables):
    minimaPonderada = 1
    minimoValor = ""
    minimaCondicion = None
    for i in listaVariables:
      condicion = self.MejorVariable(lista, i)
      ponderada = condicion[0]
      if ponderada < minimaPonderada:
        minimaPonderada = ponderada
        minimoValor = condicion[1]
        minimaCondicion = condicion[2]
  
    #print("La mejor condicion es: " + str(minimaCondicion) + " Con el valor: " + str(minimoValor)+" y su impureza es: " + str(minimaPonderada))
    parejaDeMatrices = self.dividirNodo(lista, minimaCondicion, minimoValor)
    parejaCondicion = (minimaCondicion, minimoValor)
    return (parejaDeMatrices,parejaCondicion)

  def dividirNodo(self, lista, posVariable, valor):
    primero = self.getPrimerValor(posVariable)
    laVariableEsIgualAlValor = []
    laVariableNOEsIgualAlValor = []
    for fila in lista:
      try:
        float(primero)
        condicion = float(self.dataset[fila][posVariable]) >= valor  
      except:
        condicion =  self.dataset[fila][posVariable] == valor

      if condicion:
        laVariableEsIgualAlValor.append(fila)
      else:
        laVariableNOEsIgualAlValor.append(fila)
  
    parejaDeMatrices = (laVariableEsIgualAlValor, laVariableNOEsIgualAlValor)
    return parejaDeMatrices
   
  def testear(self, datasetTest, estudiante, posVariables):  
    exito = None
    nodoActual = self.root
    pregunta = self.pregunta
    while(nodoActual.leftNode is not None and nodoActual.rightNode is not None):
      if datasetTest[estudiante][pregunta[0]] == pregunta[1]:
        nodoActual = nodoActual.leftNode.root
        try:
          pregunta = nodoActual.leftNode.pregunta 
        except:
          continue
      else:   
        nodoActual = nodoActual.rightNode.root
        try:
          pregunta = nodoActual.rightNode.pregunta 
        except:
          continue
   
    porcentajeNodo = Giny.giniImpurity.porcentajeDeExito(self.dataset, nodoActual.lista)   
    if porcentajeNodo > 99:    
      exito = 1
    else:
      exito = 0
    return exito

    
  def generarBosque(bosque, posVariables, datasetTrain, datasetTest, listaTest, listaTrain, cantArboles, sizeArbol, alturaMaxima):
    #print("Empece a crear arboles")
    timeCreacion = time.time()
    while (len(bosque) < cantArboles):
      #start_time = time.time()
      listaRef = []

      a = None
      for est in range(randbelow(sizeArbol)+10):
          listaRef.append(randbelow(len(listaTrain)))

      #print(f"Empece a crear el arbol {len(bosque)}") 
      a = ArbolDecision(listaRef, posVariables, datasetTrain, alturaMaxima = randbelow(alturaMaxima) + 3)
      #print(f"Cree el arbol {len(bosque)}")
      #end_time = time.time()
      #print('Time ' + str(end_time-start_time))
      if a is not None:
          if a.root.lista is not None:
              try:
                  a.pregunta
                  bosque.append(a)
              except:
                  continue
    endTimeCreacion = time.time()
    print('Tiempo de creacion de arboles ' + str(endTimeCreacion - timeCreacion))
  
    startTimeEvaluacion = time.time()
    falsosPositivos = 0
    falsosNegativos = 0
    verdaderosPositivos = 0
    verdaderosNegativos = 0
    for estudiantes in listaTest:
      votoExito = 0
      votoNoExito = 0
      exito = None
      for arbol in bosque:
        opinion = arbol.testear(datasetTest, estudiantes, posVariables)      
        if opinion == 1:
            votoExito += 1
        else:
            votoNoExito += 1
            

      if votoExito > votoNoExito:
        exito = 1
      else:
        exito = 0
   
      if int(datasetTest[estudiantes][77]) == exito and exito  == 1:
   
          verdaderosPositivos += 1
      elif int(datasetTest[estudiantes][77]) == exito and exito  == 0:
          verdaderosNegativos += 1
      elif int(datasetTest[estudiantes][77]) != exito and exito  == 1:
          falsosPositivos += 1
      else:
          falsosNegativos += 1         

    
    endTimeEvaluacion = time.time()
    print('Tiempo de evaluacion ' + str(endTimeEvaluacion - startTimeEvaluacion))

    print("Verdaderos Positivos: " + str(verdaderosPositivos))
    print("Verdaderos Negativos: " + str(verdaderosNegativos))
    print("Falsos Positivos: " + str(falsosPositivos))
    print("Falsos Negativos: " + str(falsosNegativos))
    print(f"Acurracy: {(verdaderosPositivos + verdaderosNegativos)/len(datasetTest):.2f}")
    print(f"Precision: {(verdaderosPositivos/(verdaderosPositivos+falsosPositivos)):.2f}")
    print(f"Recall: {(verdaderosPositivos/(verdaderosPositivos+falsosNegativos)):.2f}" )
    print('Respuesta basada en ' + str(len(bosque)) + ' arboles')