import pandas as pd

class main:
  def main():
    tree = BinaryTree()
    dataset = pd.read_csv('personas-en-situacion-de-vulnerabilidad.csv', header = 0, sep = ',')
    for i in range(len(dataset)):
      nombre = dataset['FirstName'][i] + ' ' + dataset['LastName'][i]
      numero = dataset['PhoneNumber'][i]
      tree.insertar(Persona(nombre, numero))
    f = open("Test.txt", "a")
    f.write(tree.dibujar())
    f.close()


class Persona:
  def __init__(self, nombre, numero):
	  self.nombre = nombre
	  self.numero = numero
  
  def __repr__(self):
    return f'"Contacto: {self.nombre} \\n Numero: {self.numero}"'

class Nodo:
	def __init__(self, persona):
		self.left = None
		self.right = None
		self.persona = persona

	def __repr__(self):
		return f'{self.persona}'

class BinaryTree:

  def __init__(self):
    self.root = None
  
    # ------------------------------------------------------
  def insertar(self, persona):
    if self.root is None:
      self.root = Nodo(persona)
    else:
      self.insertar_aux(persona, self.root)

  def insertar_aux(self, persona, nodo):
    if nodo == None:
      nodo = Nodo(persona)
      return nodo
    if persona.numero < nodo.persona.numero:
      nodo.left = self.insertar_aux(persona, nodo.left)
    elif persona.numero > nodo.persona.numero:
      nodo.right = self.insertar_aux(persona, nodo.right)
    return nodo

    # ------------------------------------------------------    
  def buscar(self, persona):
    return self.buscar_aux(persona.numero, self.root)

  def buscar_aux(self, numero, nodo):
    if nodo == None:
      print("Not found")
      return False
    elif nodo.persona.numero == numero:
      print("Found")
      return True
      
    if nodo.persona.numero > numero:
      return self.buscar_aux(numero, nodo.left)
    elif nodo.persona.numero < numero:
      return self.buscar_aux(numero, nodo.right)
    else:
      return False
            
  # ------------------------------------------------------
  # In-Orden        
  def imprimir(self):
    self.__imprimir_aux(self.root)
        
  def __imprimir_aux(self, actual):
    if actual is not None:
      self.__imprimir_aux(actual.left)
      print(f'{actual.persona}')
      self.__imprimir_aux(actual.right)
            
    # ------------------------------------------------------
  def dibujar(self):
    return  f'digraph G {"{"} \n {self.dibujar_aux(self.root)} \n{"}"}'
    
  def dibujar_aux(self, actual):
    if actual is None:
      return ""
    else:
      if actual.left is not None and actual.right is not None:        
        return f'{self.dibujar_aux(actual.left)} \n {self.dibujar_aux(actual.right)} \n {actual} -> {actual.left} \n {actual} -> {actual.right}'
      if actual.left is not None:    
        return f'{self.dibujar_aux(actual.left)} \n {actual} -> {actual.left}'
      if actual.right is not None:
        return f'{self.dibujar_aux(actual.right)} \n {actual} -> {actual.right}'
    return ""
      
      
       


  
if __name__ == '__main__':
  main.main()
    