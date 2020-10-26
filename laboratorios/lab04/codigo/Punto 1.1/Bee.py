import pandas as pd
class Bee:
  def __init__(self, latitude, longitude, altitude):
    self.latitude = latitude
    self.longitude = longitude
    self.altitude = altitude

  def getLatitude(self):
    return self.latitude

  def getLongitude(self):
    return self.longitude

  def getAltitude(self):
    return self.altitude
  
  def toString(self):
    return str(self.latitude) + " " +  str(self.longitude) + " " + str(self.altitude)

  def crearAbejasPorTxt(nombreArchivo):
    dataset = pd.read_csv(nombreArchivo, sep=",", header=None)
    bees = []
    for i in range(1,len(dataset)):
      latitude = float(dataset[0][i])
      longitude = float(dataset[1][i])
      altitude = float(dataset[2][i])
      bees.append(Bee(latitude, longitude, altitude))
    return bees
  
  def getMins(arrayBees):
    if len(arrayBees) <= 0:
      return None
    minLatitud = arrayBees[0].getLatitude()
    minLongitude = arrayBees[0].getLongitude()
    minAltitude = arrayBees[0].getAltitude()


    for bee in arrayBees:
      #if bee.getLatitude() < minLatitud:
        #minLatitud = bee.getLatitude()
      minLatitud = min(minLatitud, bee.getLatitude())
      minLongitude = min(minLongitude, bee.getLongitude())
      minAltitude = min(minAltitude, bee.getAltitude())
      #if bee.getLongitude() < minLongitude:
        #minLongitude = bee.getLongitude()
      #if bee.getAltitude() < minAltitude:
        #minAltitude = bee.getAltitude()
    return (minLatitud, minLongitude, minAltitude)
  
  def getMaxs(arrayBees):
    if len(arrayBees) <= 0:
      return None
    maxLatitud = arrayBees[0].getLatitude()
    maxLongitude = arrayBees[0].getLongitude()
    maxAltitude = arrayBees[0].getAltitude()
    for bee in arrayBees:
      maxLatitud = max(maxLatitud, bee.getLatitude())
      maxLongitude = max(maxLongitude, bee.getLongitude())
      maxAltitude = max(maxAltitude, bee.getAltitude())
      #if bee.getLatitude() > maxLatitud:
       # maxLatitud = bee.getLatitude()
      #if bee.getLongitude() > maxLongitude:
       # maxLongitude = bee.getLongitude()
      #if bee.getAltitude() > maxAltitude:
       # maxAltitude = bee.getAltitude()
    return (maxLatitud, maxLongitude, maxAltitude)

  def __str__(self):
    return str(self.__dict__)