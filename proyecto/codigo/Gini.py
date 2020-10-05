import numpy as np
import pandas as pd


def leerDatos(archivo):
  datos = pd.read_csv(archivo, header=0, sep=';', encoding="utf-8")
  return datos


def dividirUnaMatrizEnDosMatrices(m, posVariable, valor):
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


def ginyImpurity(m):
  alumnosExitosos = 0
  alumnosNOExitosos = 0
  for fila in range(0, len(m)):
      if int(m[fila][77]) == 1:
        alumnosExitosos += 1
      else:
        alumnosNOExitosos += 1
  proporcionExitosos = alumnosExitosos / len(m)
  proporcionNOExitosos = alumnosNOExitosos / len(m)
  impureza = 1 - (proporcionExitosos**2 + proporcionNOExitosos**2)
  #borrar linea
  print("Porcentaje de exito: " + str(alumnosExitosos*100/len(m)))
  return impureza


dataset = leerDatos('DatasetUTF-8B.csv').to_numpy()
matrices = dividirUnaMatrizEnDosMatrices(dataset, 4, "Si")
#El valor numero 4 hace referencia al dato del estudiante "estu_tomo_cursopreparacion", usado para hacer el test
matrizVariableEsValor = matrices[0]
matrizVariableNOEsValor = matrices[1]

print("%.4f" % ginyImpurity(matrizVariableEsValor))
print("%.4f" % ginyImpurity(matrizVariableNOEsValor))

print(matrizVariableEsValor.shape)
print(matrizVariableNOEsValor.shape)