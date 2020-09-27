import pandas as pd
class Estudiante:
  def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo


def consulta1(curso, semestre, dataset):
  i = 0
  print("Filtrando por Materia: "+ curso + " y Semestre: " + str(semestre))
  while i < len(dataset): 
    if (dataset["Nom. Materia"][i] == curso and dataset["Semestre"][i] == semestre):
      print("Estudiante: "+ dataset["nombre"][i] + " --- Nota final: " + str(dataset["Nota Definitiva"][i])) 
    i += 1

def consulta2(estudiante, semestre, dataset):
  i = 0 
  printAux = ""
  print("Filtrando por Estudiante: "+ estudiante.nombre + " --- codigo: "+ str(estudiante.codigo) + " --- y Semestre: " + str(semestre))
  while i < len(dataset): 
    if (dataset["nombre"][i] == estudiante.nombre and dataset["código"][i] == estudiante.codigo and dataset["Semestre"][i] == semestre) and dataset["Nom. Materia"][i] != printAux:
      print("Curso Matriculado: "+ dataset["Nom. Materia"][i] + " --- Nota final: " + str(dataset["Nota Definitiva"][i])) 
      printAux = dataset["Nom. Materia"][i]
    i += 1

#unificando los datasets
dataset = []
archivo1 = "Notas 20ST0242.csv"
datos1 = pd.read_csv(archivo1, header=0, sep=',',encoding = "UTF-8")
archivo2 = "Notas 20ST0245.csv"
datos2 = pd.read_csv(archivo2, header=0, sep=',',encoding = "UTF-8")
archivo3 = "Notas 20ST0247.csv"
datos3 = pd.read_csv(archivo3, header=0, sep=',',encoding = "UTF-8")

dataset.append(datos1)
dataset.append(datos2)
dataset.append(datos3)
frame = pd.concat(dataset, axis=0, ignore_index=True)

#datos para consulta1
curso = "FUNDAMENTOS DE PROGRAMACIÓN"
semestre = 20151

#datos para consulta2
estudiante = Estudiante("Aarón", 0)
semestre2 = 20142

#implementacion metodos
consulta1(curso, semestre, frame)
consulta2(estudiante, semestre2, frame)



