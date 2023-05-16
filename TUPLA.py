miTupla=("Jesus", 4)
miLista=list(miTupla)
print(miTupla[:])
print(miLista[:])

miLista1=["Hola","bye"]
miTupla1=tuple(miLista1)

print(miLista1[:])
print(miTupla1[:])

print("Jesus" in miTupla)
print(miTupla.count("Hola"))

print(len(miTupla))#len para saber la cantidad de elementos

tuplaUnitaria=("JEsus",)
print(tuplaUnitaria)

tuplaSinPArentesis="Juan", 1,14
print(tuplaSinPArentesis) #Empaquetado de tupla, se colocan parentesis al llamar la tupla que no lo tiene

nombre, cm, edad=tuplaSinPArentesis #Desempaquetado de tupla: asigna una a una a variables los elementos de una tupla

print(nombre, cm, edad)
