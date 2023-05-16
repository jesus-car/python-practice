print("Verificación de acceso")

while True:

	edad_usuario=int(input("Introduce tu edad: "))

	if 0<edad_usuario<18:
		print("No puedes pasar")
		break

	elif edad_usuario<1:
		print("Ingrese una edad correcta")

	else:
		print("Ud puede pasar")
		break