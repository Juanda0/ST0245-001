class Node:
    def __init__(self, data, next = None, prev = None):
        self.item = data
        self.next = next
        self.prev = prev


class doubleList:
    def __init__(self):
        self.first_node = None
        self.last_node = None
    
    def insert(self, data):
        new_node = Node(data)
        if self.first_node == None:
          self.first_node = new_node
          self.last_node = new_node
        else:
          new_node.next = self.first_node
          self.first_node.prev = new_node
          self.first_node = new_node
        
    def insertEnd(self, data):
        new_node = Node(data, prev = self.last_node)
        if self.first_node == None:
          self.first_node = new_node
          self.last_node = new_node
        else:
          self.last_node.next = new_node
          self.last_node = new_node
    
    def size(self):
      tempNode = self.first_node
      size = 0
      while(tempNode != None):
        size += 1
        tempNode = tempNode.next
      return size

    def delete(self, index):
        tempNode = self.first_node
        if index < 0 or index > self.size():
          print("indexOutOfBounds")
          return
        if index == 0:
          self.first_node = self.first_node.next  
          self.first_node.prev = None
          return
        if index == self.size():
          self.last_node = self.last_node.prev
          self.last_node.next = None
          return
        for x in range(index):
          tempNode = tempNode.next
        tempNode.prev.next = tempNode.next
        tempNode.next.prev = tempNode.prev
              
    def search(self, data):
      tempNode = self.first_node
      while(tempNode != None):
        if tempNode.item == data:
          return True
        tempNode = tempNode.next
      return False

    def show(self):
      tempNode = self.first_node
      while(tempNode != None):
        print(tempNode.item)
        tempNode = tempNode.next
      return
    
    def showButPrev(self):
      tempNode = self.last_node
      while(tempNode != None):
        print(tempNode.item)
        tempNode = tempNode.prev
      return
    
doubleListTest = doubleList()
doubleListTest.insert(3)
doubleListTest.insert(2)
doubleListTest.insert(1)
doubleListTest.insertEnd(0)
doubleListTest.insertEnd(3)
doubleListTest.insertEnd(2)
doubleListTest.insertEnd(1)
doubleListTest.show()
print("----------")
doubleListTest.delete(3)
doubleListTest.delete(2)
doubleListTest.show()
print("----------")
doubleListTest.showButPrev()

if(doubleListTest.search(1)):
  print("Se encontro weeeee")
else:
  print("Pos eso no esta wei :c")

if(doubleListTest.search(5)):
  print("Se encontro weeeee")
else:
  print("Pos eso no esta wei :c")



