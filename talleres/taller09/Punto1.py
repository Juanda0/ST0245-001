import collections

class execute:
  def main():
    hashTable = tabla()
    hashTable.put("Andrea", 3108273912)
    hashTable.put("Paco", 3134439186)
    hashTable.put("Catalina", 3152349123)
    hashTable.put("Ximena", 3132356391)
    print("The telefonic number of Andrea is: " + str(hashTable.getByKey("Andrea")))
    print("The person with the number 3132356391 is " + hashTable.getByValue(3132356391))
    
class hashData:
  def __init__(self, k, v):
    self.key = k
    self.value = v

class tabla:
  def __init__(self):
    self.tabla = [0]*10
    for i in range(0, len(self.tabla)):
     self.tabla[i] = collections.deque()
  
  def funcionHash(self, k):
    return ord(k[0]) % 10
  
  def put(self, k, v):  
    indiceLlave = self.funcionHash(k)
    self.tabla[indiceLlave].append(hashData(k, v))
  
  def getByKey(self, k):
    indiceLlave = self.funcionHash(k)
    try:
      for i in self.tabla[indiceLlave]:
        if i.key == k:
          return i.value
    except:
      return None

  def getByValue(self, v):
    try:
      for i in range(0, len(self.tabla)):
        if len(self.tabla[i]) > 0:
          for j in self.tabla[i]:
            if j.value == v:
              return j.key
    except:
      return None


if __name__ == '__main__':
    execute.main()

  