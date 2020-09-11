import pandas as pd
class Node():
 def __init__(self, data=None, nxt = None):
   self.data = data
   self.next = nxt

 def __str__(self):
   return "" + self.data

class Lsimple():
 def __init__(self):
   self.first_Node = None
   self.last_Node = None

 def __void(self):
   return self.first_Node == None
    
 
 def insert(self, element):
   tempNode = self.first_Node
   self.first_Node = Node(element)
   self.first_Node.next = tempNode

  
 def size(self):
   tempNode = self.first_Node
   count = 0
   while(tempNode != None):    
     tempNode = tempNode.next
     count += 1
   return count

 
 def remove(self, index):
   i = 1
   tempNode = self.first_Node 
   while i < index:
     tempNode = tempNode.next
     i += 1
   tempNode.next = tempNode.next.next
      
   
 def contains(self, data):
   tempNode = self.first_Node
   while tempNode != None:         
     if (tempNode.data == data):
       return True
     tempNode = tempNode.next       
   return False

 def data_Bee(self):
  tempNode = self.first_Node
  data = ""
  i = 0
  while(tempNode != None):
    data += 'abeja ' + str(i) + ' en x: ' + str(tempNode.data.x) 
    data += ' en y: ' + str(tempNode.data.y)  
    data += ' y en z: ' + str(tempNode.data.z) + '\n'
    tempNode = tempNode.next
    i += 1
  return data

 def find_Bee(self, dataF):
  count = 0
  tempNode = self.first_Node
  while(tempNode != None):
   if tempNode.data.x == dataF.x and tempNode.data.y == dataF.y and tempNode.data.z == dataF.z:
     return count
   tempNode = tempNode.next
   count += 1
  print('La abeja no se encuentra en la lista')
  
 def print(self):
  tempNode = self.first_Node
  while(tempNode != None):
    print(tempNode.data)
    tempNode = tempNode.next
  print('terminó')

class bee():
  def __init__(self,x,y,z):
    self.x = x
    self.y = y
    self.z = z
  
class __main__():
  def create_Bee_Linkedlist_From_Datasets(dataset):
    linky = Lsimple()
    data = pd.read_csv(dataset, header=0, sep=',')
    i = 0
    while i < len(data['Coordenada x de la abeja']):
      x = data['Coordenada x de la abeja'][i]
      y = data[' coordenada y de la abeja'][i]
      z = data[' coordenada z de la abeja'][i]
      bees = bee(x, y , z)
      linky.insert(bees)
      i += 1
    return linky

  intLinkedList = Lsimple()
  j = 15
  while(j > 0):
     intLinkedList.insert(j)
     j -= 1
  emptyList = Lsimple()
  #parametro del metodo es el nombre del csv, cambiarlo en caso de querer probar uno mas grande
  beesLinkedList = create_Bee_Linkedlist_From_Datasets('dataset10D.csv')
  beeAlfa = bee(-75.5616007379, 6.32870576905, 1628.36)
  beeBeta = bee(0,1,2)
  #se recomienda remover el print(i.data_Bee...) en datasets grandes 
  print(beesLinkedList.data_Bee() + '\nSearchinnnnnng')
  print(beesLinkedList.find_Bee(beeAlfa))
  print(beesLinkedList.find_Bee(beeBeta))
  
