import collections
class main():

    keyboardList = collections.deque([])
    text = "asd[gfh[[dfh]hgh]fdfhd[dfg[d]g[d]dg"
    addAux = 0      
    i = 0
    dataAux = ""  
    while i < len(text):
      if text[i] == "[":
        if addAux == 0:
          keyboardList.appendleft(dataAux)
        else:
          keyboardList.append(dataAux)
        dataAux = ""   
        addAux = 0    
        i += 1  
      elif text[i] == "]":
        if addAux == 0:
          keyboardList.appendleft(dataAux)
        else:
          keyboardList.append(dataAux) 
        dataAux = ""        
        addAux = 1
        i += 1    
      else:             
        dataAux+=text[i]     
        i += 1        
    if addAux == 0:
      keyboardList.appendleft(dataAux)
    else:
      keyboardList.append(dataAux)
    data = ""
    for letter in keyboardList:
      data += letter
    print (data)
    