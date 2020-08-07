i = 0
j = 0
def subconjuntosBase(base, palabra):
    if len(palabra) == 0:       
        print (base)
    else:
        subconjuntosBase(base + palabra[i],palabra[i+1:len(palabra)])
        subconjuntosBase(base, palabra[j+1:len(palabra)])
        
       
def subconjuntos(s):
    subconjuntosBase("", s)

 


print(subconjuntos("Alex"))
print(subconjuntos("Santi"))
print(subconjuntos("abc"))

#profe, no logramos eliminar el "None" de la impresion :c. Supongamos que no exite c:
#si sabes ayudanos :c
