import numpy as np
import pandas as pd
      
#Procesa el dataset
def leerDatos(archivo):
  datos = pd.read_csv(archivo, header=0, sep=';', encoding="utf-8")
  return datos

#Retorna la media de una variable (eje: el promedio de matematicas)
def media(m, posVariable):
  total = 0
  for fila in range(0, len(m)):
    total += float(m[fila][posVariable])
  return total/len(m)

#llama dividir una matriz en dos matrices de acuerdo al tipo de dato
def dividirUnaMatrizEnDosMatrices(m, posVariable, valor):
  i = 0
  primero = m[0][posVariable]
  #Si el primero es "nan", busca el primer valor en la lista con un valor real
  if type(primero) is float:
    if np.isnan(primero):
      for fila in m:
        primero = m[i][posVariable]
        try:
          if np.isnan(primero):
            i += 1
            continue
          break     
        except:
          break

  if type(primero) is str:
    return dividirUnaMatrizEnDosMatricesStr(m, posVariable, valor)
  else:
    return dividirUnaMatrizEnDosMatricesInt(m, posVariable, valor)

#divide una matriz de acuerdo a una condicion que utiliza enteros
def dividirUnaMatrizEnDosMatricesInt(m, posVariable, valor):
  valor = int(media(m, posVariable)) + 1
  print("Media es: " + str(valor))
  laVariableEsIgualAlValor = 0
  for fila in range(0, len(m)):
    if m[fila][posVariable] >= valor:
      laVariableEsIgualAlValor += 1
  
  laVariableNOEsIgualAlValor = len(m) - laVariableEsIgualAlValor
  matrizVariableEsValor = np.zeros((laVariableEsIgualAlValor, len(m[0])), dtype=object)
  matrizVariableNOEsValor = np.zeros((laVariableNOEsIgualAlValor, len(m[0])), dtype=object)
  i = 0
  j = 0
  for fila in range(0, len(m)):
    if m[fila][posVariable] >= valor:
      matrizVariableEsValor[i] = m[fila]
      i += 1
    else:
      matrizVariableNOEsValor[j] = m[fila]
      j += 1
  parejaDeMatrices = [matrizVariableEsValor, matrizVariableNOEsValor]
  return parejaDeMatrices

#divide una matriz de acuerdo a una condicion que utiliza strings
def dividirUnaMatrizEnDosMatricesStr(m, posVariable, valor):
  laVariableEsIgualAlValor = 0
  for fila in range(0, len(m)):
    if m[fila][posVariable] == valor:
      laVariableEsIgualAlValor += 1

  laVariableNOEsIgualAlValor = len(m) - laVariableEsIgualAlValor
  matrizVariableEsValor = np.zeros((laVariableEsIgualAlValor, len(m[0])), dtype=object)
  matrizVariableNOEsValor = np.zeros((laVariableNOEsIgualAlValor, len(m[0])), dtype=object)
  i = 0
  j = 0
  for fila in range(0, len(m)):
    if m[fila][posVariable] == valor:
      matrizVariableEsValor[i] = m[fila]
      i += 1
    else:
      matrizVariableNOEsValor[j] = m[fila]
      j += 1
  parejaDeMatrices = [matrizVariableEsValor, matrizVariableNOEsValor]
  return parejaDeMatrices

#Retorna los posibles valores que puede usar una columna
def posiblesCondiciones(m, posVariable):
  valores = []
  try:
    valores.append(int(media(m, posVariable)) + 1)
  except: 
    for fila in range(0, len(m)):
      valor = m[fila][posVariable]
      condition = True
      for pos in valores:
        if valor == pos:
          condition = False 
          break
      if condition and type(valor) is str: 
        valores.append(valor)
  return valores

#calcula la impureza de una matriz
#Dentro del for se realizaron diferentes condiciones para eliminar los estudiantes que respondieron la pregunta
#Recordar que el dataset esta lleno de valores "nan" gracias al metodo de numpy, por ello, con las condiciones se busca eliminar estos "nan"
def ginyImpurity(m, posVariable):
  alumnosExitosos = 0
  alumnosNOExitosos = 0
  alumnosNoRespondieron = 0
  for fila in range(0, len(m)):
      if int(m[fila][77]) == 1:
        alumnosExitosos += 1
        continue
      elif type(m[fila][posVariable]) is not float:
        alumnosNOExitosos += 1
        continue
      elif m[fila][posVariable] >= 0:
        alumnosNOExitosos += 1
      else:
        alumnosNoRespondieron += 1
  if alumnosNoRespondieron > 0:
    print(str(alumnosNoRespondieron) + " No respondieron esta pregunta y fueron excluidos de la impureza")
  proporcionExitosos = alumnosExitosos / (alumnosExitosos + alumnosNOExitosos)
  proporcionNOExitosos = alumnosNOExitosos / (alumnosExitosos + alumnosNOExitosos)
  impureza = 1 - (proporcionExitosos**2 + proporcionNOExitosos**2)
  #borrar linea
  return impureza

#calcula la impureza ponderada de dos matrices
def ginyImpurityWeightened(matriz1, matriz2, posVariable):
  impureza1 = ginyImpurity(matriz1, posVariable)
  impureza2 = ginyImpurity(matriz2, posVariable)
  tamaño1 = len(matriz1)
  tamaño2 = 0
  for fila in range(0, len(matriz2)):
      if type(matriz2[fila][posVariable]) is not float:
        tamaño2 += 1
        continue
      elif matriz2[fila][posVariable] >= 0:
        tamaño2 += 1
  impurezaPonderada = ((tamaño1*impureza1)+(tamaño2*impureza2))/(tamaño1 + tamaño2)
  return impurezaPonderada

#calcula el porcentaje de exito de una matriz
def porcentajeDeExito(m):
  alumnosExitosos = 0
  alumnosNOExitosos = 0
  for fila in range(0, len(m)):
      if int(m[fila][77]) == 1:
        alumnosExitosos += 1
      else:
        alumnosNOExitosos += 1
  return alumnosExitosos*100/len(m)

#calcula la condicion que mejor reduce la impureza de una columnna
def menorImpurezaPonderadaPorVariable(m, posVariable):
  variables = posiblesCondiciones(m, posVariable)
  menorCondicion = ""
  menorImpureza = 1
  #si se cumple la condicion, significa que la variable a usar es un entero
  if len(variables) == 1:
    matrices = dividirUnaMatrizEnDosMatrices(m, posVariable, variables[0])
    matriz1 = matrices[0]
    matriz2 = matrices[1]
    impureza = ginyImpurityWeightened(matriz1, matriz2, posVariable)
    print("Se calculó la impureza ponderada de acuerdo al promedio de las variables debido a que es una variable numerica. La impureza es: %.4f" % impureza)
    return variables[0]
  for condicion in variables:
    matrices = dividirUnaMatrizEnDosMatrices(m, posVariable, condicion)
    matriz1 = matrices[0]
    matriz2 = matrices[1]
    impureza = ginyImpurityWeightened(matriz1, matriz2, posVariable)
    print("Para la condicion: "+ str(condicion) +" la impureza es: %.4f" % impureza)
    if impureza < menorImpureza:
      menorCondicion = condicion
      menorImpureza = impureza
  return menorCondicion

#El valor numero 4 hace referencia al dato del estudiante "estu_tomo_cursopreparacion", usado para hacer el test
#El valor numero 54 hace referencia al dato del estudiante "Colegio bilingue", usado para hacer el test
#El valor numero 65 hace referencia al dato del estudiante "puntaje Lenguaje", usado para hacer el test
dataset = leerDatos('DatasetUTF-8B.csv').to_numpy()
#Arreglo contiene posiciones a testear 
posVariables = [4]
for i in posVariables:
    #Imprimime la condicion con menor impureza
    print(posiblesCondiciones(dataset, i))
    print("La condicion con menor impureza ponderada es: " + str(menorImpurezaPonderadaPorVariable(dataset, i)))

