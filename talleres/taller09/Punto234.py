def main():
  tablaDatos = {"Google" : "Estados Unidos", "La locura" : "Colombia", "Nokia" : "Finlandia", "Sony" : "Japón"} 
  findPaisPorEmpresa(tablaDatos, "Google")
  findPaisPorEmpresa(tablaDatos, "Motorola")
  findEmpresaPorPais(tablaDatos, "Estados Unidos")
  findEmpresaPorPais(tablaDatos, "india")
def findPaisPorEmpresa(tablaDatos, llave):
  try:
   print("El pais correspondiente a la empresa es: " + tablaDatos[llave])
  except:
    print("No se encontró coincidencia")
  
def findEmpresaPorPais(tablaDatos, pais):
  try:
    key_list = list(tablaDatos.keys()) 
    val_list = list(tablaDatos.values())
    print("Las empresas de ese país son: " + key_list[val_list.index(pais)])
  except:
    print("No se encontró coincidencia")

if __name__ == "__main__":
  main()