class Main:
  def main (): 	
    test = [50,30,24,5,28,45,98,52,60]
    arbolitou = Tree()
    arbolitou.buildingTree(test)
    print("Para el recorrido en preorden de un arbol")
    arbolitou.preOrder()
    print("\nEl PosOrder es: ")
    arbolitou.posOrder()
    
class Node: 
  def __init__(self, data , left = None, right = None):
    self.left = None
    self.right = None
    self.data = data

class Tree:	
  def __init__(self, root = None):
    self.root = root

  def buildingTree (self, preOrder): 
    self.root=Node(preOrder[0])
    for i in range (1, len(preOrder)):
      self.insert(self.root, preOrder[i])

  def insert (self, node, data): 
    if data < node.data and node.left is None: 
      node.left = Node(data)

    elif data > node.data and node.right is None: 
      node.right = Node(data)
      
    elif data < node.data and node.left is not None: 
      self.insert(node.left, data)
    
    elif data > node.data and node.right is not None: 
      self.insert(node.right, data)

  def preOrder(self):
    Tree.preOrderAux(self.root)

  def posOrder(self):
    Tree.posOrderAux(self.root)

  def preOrderAux(node): 
    if node is not None: 
      print(node.data),	
      Tree.preOrderAux(node.left)
      Tree.preOrderAux(node.right)

  def posOrderAux(node):
    if node is not None:
      Tree.posOrderAux(node.left)
      Tree.posOrderAux(node.right)
      print(node.data)

if __name__ == "__main__":
	Main.main()
  
  
