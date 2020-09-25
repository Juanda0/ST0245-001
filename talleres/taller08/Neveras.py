import collections

class nevera:
  def __init__(self, codigo, marca):
    self.codigo = codigo
    self.marca = marca

  def neveraData(self):
    return ('(' + str(self.codigo) + ', ' + self.marca + ')')
    
class solicitud():
  def __init__(self, empresa, noNeveras):
    self.empresa = empresa
    self.noNeveras = noNeveras
    
def asignarSolicitudes(neverasS,solicitudesQ):
  if len(neverasS) == 0 or len(solicitudesQ) == 0: return
  neverasSCopy = neverasS
  solicitudesQCopy = solicitudesQ
  neverasSolicitadas = []
  solicitud = solicitudesQCopy.pop()
  i = 0
  while (len(neverasSCopy) != 0) and i < solicitud.noNeveras:
    nevera = neverasSCopy.popleft()
    neverasSolicitadas.append(nevera.neveraData())
    i += 1 
  stringNevera = " ["
  for element in neverasSolicitadas:
    stringNevera +=  element + ','
  stringNevera = stringNevera[:len(stringNevera)-1]
  stringNevera += "]"
  print(solicitud.empresa + stringNevera)
  return asignarSolicitudes(neverasSCopy,solicitudesQCopy)

neverasS = collections.deque()
neverasS.appendleft(nevera(1,'Haceb'))
neverasS.appendleft(nevera(2,'LG'))
neverasS.appendleft(nevera(3,'IBM'))
neverasS.appendleft(nevera(4,'Haceb'))
neverasS.appendleft(nevera(5,'LG'))
neverasS.appendleft(nevera(6,'IBM'))
neverasS.appendleft(nevera(7,'Haceb'))
neverasS.appendleft(nevera(8,'LG'))
neverasS.appendleft(nevera(9,'IBM'))
neverasS.appendleft(nevera(8,'LG'))
neverasS.appendleft(nevera(9,'IBM'))

solicitudesQ = collections.deque([])
solicitudesQ.append(solicitud('¬ Eafit    ',10))
solicitudesQ.append(solicitud('¬ La14     ',2))
solicitudesQ.append(solicitud('¬ Olimpica ',4))
solicitudesQ.append(solicitud('¬ Éxito    ',1))


asignarSolicitudes(neverasS,solicitudesQ)

#Para stack solo se usaron los metodos appendleft y popleft,
#Para colas solo se usaron los metodos append y pop
#NeverasS es un stack de neveras
#SolicitudesQ es una queue de solicitudes 

