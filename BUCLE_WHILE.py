import math

numero=int(input("Introduce un número: "))
intentos=0
while numero<0:
	print("No se puede calcular")

	if intentos==2:

		print("Ya no puede seguir intentando")
		break

	numero=int(input("Vuelva a intentarlo"))

	if numero<0:
		intentos=intentos+1

if intentos<2:
	solucion=math.sqrt(numero)
	print(f"La raiz cuadrada de {numero} es {solucion}")
