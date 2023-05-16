miDiccionario={"clave":"hola", "clave1":25, 1996:"Jesus"}

miDiccionario["Italia"]="Lisboa"

print(miDiccionario[1996])

print(miDiccionario)

miDiccionario["Italia"]="Roma"

print(miDiccionario["Italia"])

del miDiccionario["clave"] #Para eliminar se usa del y solo la clave del diccionario

print(miDiccionario)

#Se puede usar una tupla como claves para un diccionario usando en la zona clave cada elemento de la tupla

#La clave funciona como una variable, a la cual se le puede asignar tuplas u otro diccionario

print(miDiccionario.keys()) #Devuelve las claves dle diccionario
print(miDiccionario.values()) #Devuelve los valores
print(len(miDiccionario)) #Cantidad de elementos

print(miDiccionario.pop(1996))
print(miDiccionario)