
#/usr/bin/python

class ArrayList:
 def __init__(self):
    self.__elements = []

 def size(self):
   return len(self.__elements)

 def get(self, index):
   try:
    return self.__elements[index]
   except:
     print("El indice no existe")

 def add(self, object):
   self.__elements.append(object)

 def addInIndex(self, index, object):
    self.__elements = self.__elements[:index]+[object]+self.__elements[index:]
    

 def removeInIndex(self, index):
	 self.__elements = self.__elements[:index] + self.__elements[index+1:]
 def print(self):
   print(self.__elements)

  
arr = ArrayList()
arr.add(23)
arr.print()
