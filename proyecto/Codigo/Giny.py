class giniImpurity:
  #calcula la impureza de una lista
  def ginyImpurity(dataset, lista):
    if lista is None:
        return None
    alumnosExitosos = 0
    alumnosNOExitosos = 0
    for estudiante in lista:
        if int(dataset[estudiante][77]) == 1:
          alumnosExitosos += 1
        else:
          alumnosNOExitosos += 1
    return giniImpurity.ginyImpurityAux(alumnosExitosos, alumnosNOExitosos)

  def ginyImpurityAux(alumnosExitosos, alumnosNOExitosos):
    if alumnosExitosos + alumnosNOExitosos == 0:
        return 0
    proporcionExitosos = alumnosExitosos / (alumnosExitosos + alumnosNOExitosos)
    proporcionNOExitosos = alumnosNOExitosos / (alumnosExitosos + alumnosNOExitosos)
    impureza = 1 - (proporcionExitosos**2 + proporcionNOExitosos**2)
    return impureza

  #calcula la impureza ponderada de dos listas
  def ginyImpurityWeightened(dataset, lista1, lista2):
    impureza1 = giniImpurity.ginyImpurity(dataset, lista1)
    impureza2 = giniImpurity.ginyImpurity(dataset, lista2)
    tamaño1 = len(lista1)
    tamaño2 = len(lista2)
    return giniImpurity.ginyImpurityWeightenedAux(dataset, tamaño1, tamaño2, impureza1, impureza2)

  def ginyImpurityWeightenedAux(tamaño1, tamaño2, impureza1, impureza2):
    impurezaPonderada = ((tamaño1*impureza1)+(tamaño2*impureza2))/(tamaño1 + tamaño2)
    return impurezaPonderada

  def porcentajeDeExito(dataset, lista):
    alumnosExitosos = 0
    for estudiante in lista:
        if int(dataset[estudiante][77]) == 1:
          alumnosExitosos += 1
    return (alumnosExitosos*100)/len(lista)