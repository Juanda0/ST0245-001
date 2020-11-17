class node:
  def __init__(self, lista, leftNode = None, rightNode = None):
    self.lista = lista
    if len(self.lista) == 0:
      self.lista = None
    self.leftNode = leftNode
    self.rightNode = rightNode
